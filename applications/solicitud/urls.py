# urls.py

from django.urls import path
from .views import solicitud_pdf_view

urlpatterns = [
    # otras URLs
    path('pdf/solicitud/<int:pk>/', solicitud_pdf_view, name='solicitud_pdf'),
]
