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
from .models import Proveedor


class ProveedorListView(ListView):
    model = Proveedor
    queryset = Proveedor.objects.all()


class ProveedorDetailView(DetailView):
    model = Proveedor


class ProveedorCreateView(SuccessMessageMixin, CreateView):
    model = Proveedor
    fields = ["nombre", "familia_productos", "direccion", "pedido_minimo", "telefono", "correo_electronico"]
    success_url = reverse_lazy("proveedor-list")
    success_message = "El proveedor fue creado exitosamente"


class ProveedorUpdateView(SuccessMessageMixin, UpdateView):
    model = Proveedor
    fields = ["nombre", "familia_productos", "direccion", "pedido_minimo", "telefono", "correo_electronico"]
    success_message = "El proveedor fue actualizado exitosamente"

    def get_success_url(self):
        return reverse_lazy("proveedor-detail", kwargs={"pk": self.object.id})


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    success_url = reverse_lazy("proveedor-list")
    success_message = "El proveedor fue eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
