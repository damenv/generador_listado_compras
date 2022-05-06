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
from .models import Producto
from comun.importador_csv.ImportadorCSV import ImportadorCSV
from .forms import ProductoForm

class ProductoListView(ListView):
    model = Producto
    queryset = Producto.objects.all()


class ProductoDetailView(DetailView):
    model = Producto


class ProductoCreateView(SuccessMessageMixin, CreateView):
    model = Producto
    fields = ["producto", "precio", "iva", "cantidad", "unidad_medida", "proveedor"]
    success_url = reverse_lazy("producto-list")
    success_message = "El producto fue creado exitosamente"


class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    model = Producto
    fields = ["producto", "precio", "iva", "cantidad", "unidad_medida", "proveedor"]
    success_message = "El producto fue actualizado exitosamente"

    def get_success_url(self):
        return reverse_lazy("producto-detail", kwargs={"pk": self.object.id})


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy("producto-list")
    success_message = "El producto fue eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

def upload_csv(request):
    importador = ImportadorCSV("Producto", ProductoForm.base_fields)
    return importador.upload_csv(request, "producto")
