from django.contrib import admin
from .models import Entrada, DetalleEntrada

class DetalleEntradaInline(admin.TabularInline):
    model = DetalleEntrada
    extra = 1

class EntradaAdmin(admin.ModelAdmin):
    list_display = ('requisition', 'entrydate', 'observation')
    inlines = [DetalleEntradaInline]


class DetalleEntradaAdmin(admin.ModelAdmin):
    list_display = ('entrada', 'insumo', 'cant')

admin.site.register(Entrada, EntradaAdmin)
