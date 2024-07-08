from django.contrib import admin
from .models import Cargo, Servicio, Solicitante

# Register your models here.

class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'id',
        'name',
    )
    list_filter = (
        'id',
        'name',
    )
class ServicioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'numberofemployers',
    )
    search_fields = ( 
        'id',
        'name',
    )
    list_filter = (
        'id',
        'name',
    )
class SolicitanteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'firstname',
        'edad',
    )
    search_fields = (
        'id',
        'firstname',
    )
    list_filter= (
        'id',
        'firstname',
    )
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Solicitante, SolicitanteAdmin) 