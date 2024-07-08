from django.db import models
from applications.insumos.models import Insumos

# Create your models here.
class Entrada(models.Model):
    requisition = models.BigIntegerField(verbose_name='Requisición')
    entrydate  = models.DateField('Fecha de Entrada', auto_now=False, auto_now_add=False)
    observation = models.TextField('Observacion', max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.requisition)
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

class DetalleEntrada(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumos, on_delete=models.CASCADE)
    cant = models.IntegerField(default=0)

    def __str__(self):
        return self.insumo.name
    
    def save(self, *args, **kwargs):
        if self.insumo.stock is None:
            self.insumo.stock = 0

        if not self.pk:
            # Si es una nueva instancia (no tiene primary key), suma la cantidad al stock del insumo
            self.insumo.stock += self.cant
        else:
            # Si es una instancia existente, calcula la diferencia y actualiza el stock en consecuencia
            original = DetalleEntrada.objects.get(pk=self.pk)
            difference = self.cant - original.cant
            self.insumo.stock += difference
        self.insumo.save()
        super(DetalleEntrada, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Detalle de Entrada'
        verbose_name_plural = 'Detalle de Entradas'