# views.py

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Solicitud
from applications.centro.models import Centro

def solicitud_pdf_view(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    detalle_solicitud = solicitud.detallesolicitud_set.all()
    total_general = sum(detalle.total() for detalle in detalle_solicitud)
    html_string = render_to_string('solicitud/solicitud_pdf.html', {
        'solicitud': solicitud,
        'detalle_solicitud': detalle_solicitud,
        'total_general': total_general,
    })
    
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=solicitud_{solicitud.requisition}.pdf'
    return response
