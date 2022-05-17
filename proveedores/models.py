from django.db import models
from django.core.validators import RegexValidator, EmailValidator

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=75)
    familia_productos = models.CharField(max_length=75)
    direccion = models.CharField(max_length=100, blank=True)
    pedido_minimo = models.FloatField(default=0.0)

    telefono_regex = RegexValidator(regex=r'^$|^\+?1?\d{9,15}$',
                                    message="Telefono debe introducirse en el formato: '+999999999'. "
                                            "Se aceptan hasta 15 dígitos.")
    telefono = models.CharField(validators=[telefono_regex], max_length=17, blank=True)

    email_validator = EmailValidator(message='Introducir un correo válido')
    correo_electronico = models.CharField(validators=[email_validator], max_length=254, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Proveedores"
