from django.contrib import admin
from .models import Centro


class CentroAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'jefe',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )

admin.site.register(Centro, CentroAdmin)