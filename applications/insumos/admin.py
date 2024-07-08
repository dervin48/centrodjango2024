from django.contrib import admin
from .models import Categoria, Insumos


class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'id',
    )

class InsumosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'stock',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
        'id',
    )




admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Insumos, InsumosAdmin)