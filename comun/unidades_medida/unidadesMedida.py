from django.utils.translation import gettext_lazy as _
from django.db import models

class unidadesMedida(models.TextChoices):

    # Peso
    GRAMO = 'g', _('gramos')
    KILOGRAMO = 'kg', _('kilogramos')

    # VOLUMEN
    LITRO = 'l', _('litros')

    # OTRO
    UNIDAD = 'u', _('unidades')
