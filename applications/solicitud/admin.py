from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from .models import Solicitud, DetalleSolicitud
from .views import solicitud_pdf_view  # Importar la vista correcta

class DetalleSolicitudInline(admin.TabularInline):
    model = DetalleSolicitud
    extra = 1

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('requisition', 'shipmentdate','solicitud_servicio')
    inlines = [DetalleSolicitudInline]
    actions = ['generate_pdf']

    def generate_pdf(self, request, queryset):
        if queryset.count() == 1:
            solicitud = queryset.first()
            return redirect('solicitud_pdf', pk=solicitud.pk)
        else:
            self.message_user(request, "Por favor, selecciona una única solicitud.")
    generate_pdf.short_description = "Generar PDF de la Solicitud"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('pdf/solicitud/<int:pk>/', self.admin_site.admin_view(solicitud_pdf_view), name='solicitud_pdf'),
        ]
        return custom_urls + urls

# @admin.register(DetalleSolicitud)
# class DetalleSolicitudAdmin(admin.ModelAdmin):
#     list_display = ('insumo', 'cant')
