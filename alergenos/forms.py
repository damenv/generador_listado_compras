from django import forms
from alergenos.models import Alergeno


class AlergenoForm(forms.ModelForm):

    class Meta:
        model = Alergeno
        fields = ['alergeno']
