from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Elaboracion
from comun.importador_csv.ImportadorCSV import ImportadorCSV
from .forms import ElaboracionForm


class ElaboracionListView(ListView):
    model = Elaboracion
    queryset = Elaboracion.objects.all().order_by("-fecha_creado")

class ElaboracionDetailView(DetailView):
    model = Elaboracion

class ElaboracionCreateView(SuccessMessageMixin, CreateView):
    model = Elaboracion
    fields = ["nombre", "tamano_racion", "numero_raciones", "tiempo_produccion",
              "familia", "formato", "sabor", "producto_base", "preparacion",
              "link_foto", "alergenos"]
    success_url = reverse_lazy("elaboracion-list")
    success_message = "La elaboración fue creado exitosamente"


class ElaboracionUpdateView(SuccessMessageMixin, UpdateView):
    model = Elaboracion
    fields = ["nombre", "tamano_racion", "numero_raciones", "tiempo_produccion",
              "familia", "formato", "sabor", "producto_base", "preparacion",
              "link_foto", "alergenos", "fecha_actualizado"]
    success_message = "La elaboración fue actualizado exitosamente"

    def get_success_url(self):
        return reverse_lazy("elaboracion-detail", kwargs={"pk": self.object.id})


class ElaboracionDeleteView(DeleteView):
    model = Elaboracion
    success_url = reverse_lazy("elaboracion-list")
    success_message = "La elaboracion fue eliminada exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

def upload_csv(request):
    importador = ImportadorCSV("elaboracion", ElaboracionForm.base_fields)
    return importador.upload_csv(request)
