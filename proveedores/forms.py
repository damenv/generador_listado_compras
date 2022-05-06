from django import forms
from proveedores.models import Proveedor


class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = '__all__'
