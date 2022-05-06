from django import forms
from ingredientes.models import Ingrediente


class IngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = '__all__'
