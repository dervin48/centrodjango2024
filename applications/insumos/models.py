from django.db import models

class Categoria(models.Model):
    name = models.CharField('Nombre Categoria', max_length=50)
    description = models.CharField('Descripción', max_length=150, blank=True, null=True )

    def __str__(self):
        return str(self.id) + ' '+ self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Insumos(models.Model):
    name = models.CharField('Nombre Insumo', max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    price= models.DecimalField('Precio', max_digits=5, decimal_places=2, blank=True, null=True)
    batch = models.CharField('Lote', max_length=50, blank=True)
    dudedate  = models.DateField('Fecha de Vencimiento', auto_now=False, auto_now_add=False, blank=True, null=True)   
    stock = models.IntegerField(blank=True, null=True, default=0)


    def __str__(self):
        return str(self.id) +''+ self.name + '' + str(self.price) + ''+ str(self.stock)

    class Meta:
        verbose_name ='Insumo'
        verbose_name_plural = 'Insumos'