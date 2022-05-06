from django import forms
from elaboraciones.models import Elaboracion


class ElaboracionForm(forms.ModelForm):

    class Meta:
        model = Elaboracion
        exclude = ['fecha_creado', "fecha_actualizado"]
