from django.shortcuts import render
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
from comun.importador_csv.ImportadorCSV import ImportadorCSV
from .forms import AlergenoForm

# Create your views here.
from .models import Alergeno


class AlergenoListView(ListView):
    model = Alergeno
    queryset = Alergeno.objects.all()


class AlergenoDetailView(DetailView):
    model = Alergeno


class AlergenoCreateView(SuccessMessageMixin, CreateView):
    model = Alergeno
    fields = ["alergeno"]
    success_url = reverse_lazy("alergeno-list")
    success_message = "El alergeno fue creado exitosamente"


class AlergenoUpdateView(SuccessMessageMixin, UpdateView):
    model = Alergeno
    fields = ["alergeno"]
    success_message = "El alergeno fue actualizado exitosamente"
    
    def get_success_url(self):
        return reverse_lazy("alergeno-detail", kwargs={"pk": self.object.pk})
    
class AlergenoDeleteView(DeleteView):
    model = Alergeno
    success_url = reverse_lazy("alergeno-list")
    success_message = "El alergeno fue eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

def upload_csv(request):
    importador = ImportadorCSV("Alergeno", AlergenoForm.base_fields)
    return importador.upload_csv(request, "alergeno")