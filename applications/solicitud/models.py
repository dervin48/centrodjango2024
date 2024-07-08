from django.db import models
from django.forms import ValidationError
from applications.solicitante.models import Solicitante
from applications.insumos.models import Insumos
from applications.centro.models import Centro

class Solicitud(models.Model):
    requisition = models.BigIntegerField(verbose_name='Requisición')
    applicationdate = models.DateField("Fecha de Solicitud", auto_now=False, auto_now_add=False)
    shipmentdate = models.DateField("Fecha de Despacho", auto_now=False, auto_now_add=False)
    applicant = models.ForeignKey(Solicitante, verbose_name="Solicitante", on_delete=models.CASCADE )
    observation = models.TextField('Observacion', max_length=200, blank=True, null=True)

    def __str__(self):
        formatted_date = self.shipmentdate.strftime('%d/%m/%Y')
        return f"{self.applicant.firstname} {formatted_date}"
    
    def solicitud_servicio(self):
        return self.applicant.servicio
    solicitud_servicio.short_description = "Solicitud Servicio"

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'


class DetalleSolicitud(models.Model):
    Solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumos, on_delete=models.CASCADE)
    cant = models.IntegerField(default=0)

    

    def __str__(self):
        return self.insumo.name
    
    def save(self, *args, **kwargs):
        if self.insumo.stock is None:
            self.insumo.stock = 0

        if not self.pk:
            self.insumo.stock -= self.cant
        if not self.pk:
            if self.insumo.stock < self.cant:
                raise ValidationError("Stock no alcanza para despacho.")
            self.insumo.stock -= self.cant
        else:
            original = DetalleSolicitud.objects.get(pk=self.pk)
            difference = self.cant - original.cant
            if self.insumo.stock + original.cant < self.cant:
                raise ValidationError("Stock no alcanza para despacho.")
            self.insumo.stock -= difference
        self.insumo.save()
        super(DetalleSolicitud, self).save(*args, **kwargs)
    
    def total(self):
        return self.insumo.price * self.cant

    class Meta:
        verbose_name = 'Detalle de Solicitud'
        verbose_name_plural = 'Detalle de Solicitud'
