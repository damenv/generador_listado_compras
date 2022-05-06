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

# Create your views here.
from .models import Ingrediente, Elaboracion
from comun.importador_csv.ImportadorCSV import ImportadorCSV
from .forms import IngredienteForm


class IngredienteListView(ListView):
    model = Ingrediente
    queryset = Ingrediente.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IngredienteListView, self).get_context_data(**kwargs)
        context['elaboracion_list'] = Elaboracion.objects.all()
        return context


class IngredienteDetailView(DetailView):
    model = Ingrediente


class IngredienteCreateView(SuccessMessageMixin, CreateView):
    model = Ingrediente
    fields = '__all__'
    success_url = reverse_lazy("ingrediente-list")
    success_message = "El ingrediente fue creado exitosamente"


class IngredienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Ingrediente
    fields = '__all__'
    success_message = "El ingrediente fue actualizado exitosamente"

    def get_success_url(self):
        return reverse_lazy("ingrediente-detail", kwargs={"pk": self.object.id})


class IngredienteDeleteView(DeleteView):
    model = Ingrediente
    success_url = reverse_lazy("ingrediente-list")
    success_message = "El ingrediente fue eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

def upload_csv(request):
    importador = ImportadorCSV("Ingrediente", IngredienteForm.base_fields)
    return importador.upload_csv(request, "ingrediente")
