from django.db import models
from datetime import date

class Cargo(models.Model):
    name= models.CharField('Nombre Cargo', max_length=80)
    description = models.CharField('Descripcion Cargo', max_length=80, null=True, blank=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = "Cargos"

class Servicio(models.Model):
    name = models.CharField('Nombre del Servicio', max_length=100)
    address = models.CharField('Direccion del Servicio', max_length=100, blank=True, null=True)
    numberofemployers = models.IntegerField('Numeros de Trabjadores', blank=True, null=True)

    def __str__(self):
        return  self.name
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

class Solicitante(models.Model):
    firstname = models.CharField("Nombres", max_length=80)
    lastname = models.CharField("Apellidos", max_length=80)
    birthofdate = models.DateField("Fecha de Nacimiento", auto_now=False, auto_now_add=False)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    edad = models.IntegerField(2)

    def __str__(self):
        return self.firstname +' '+ self.lastname
    
    def nombre_completo(self):
        return self.firstname + " " + self.lastname
    
    def calcular_edad(self):
        hoy = date.today()
        return hoy.year - self.birthofdate.year - ((hoy.month, hoy.day) < (self.birthofdate.month, self.birthofdate.day))

    edad = calcular_edad;
    
    class Meta:
        verbose_name = "Solicitante"
        verbose_name_plural="Solicitantes"