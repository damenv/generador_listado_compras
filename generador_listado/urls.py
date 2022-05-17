from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name='generador_listado/homepage.html'), name='home'),
    path("resultados/<int:elaboracion>", views.resultados, name='hoja-resultados'),
]