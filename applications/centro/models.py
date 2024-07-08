from django.db import models
from applications.solicitante.models import Solicitante


class Centro(models.Model):
    name = models.CharField("Nombre de Centro de Salud", max_length=80, blank=True, null=True)
    description = models.CharField("Descripcion", max_length=100, blank=True, null=True)
    jefe = models.ForeignKey(Solicitante, verbose_name="Director de Servicio", on_delete=models.CASCADE, related_name='jefe_centros')
    encargado_de_bodega = models.ForeignKey(Solicitante, verbose_name="Encargado de Bodega", on_delete=models.CASCADE, related_name='encargado_centros')
    logo = models.ImageField(upload_to="logo",  max_length=None, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.jefe}"
    
    def encargado_de_bodega(self):
        return f"{self.name} {self.encargado_de_bodega}"
    
    def jefe(self):
        return self.jefe

    class Meta:
        verbose_name = "Centro de Salud"
        verbose_name_plural ="Centros de Salud"