from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from alergenos.models import Alergeno

class Elaboracion(models.Model):
    nombre = models.CharField(max_length=75)
    tamano_racion = models.FloatField(default=1.0) #gramos
    numero_raciones = models.FloatField(default=1.0)
    tiempo_produccion = models.FloatField(default=0) #horas
    familia = models.CharField(max_length=25, blank=True)
    formato = models.CharField(max_length=25, blank=True)
    sabor = models.CharField(max_length=25, blank=True)
    producto_base = models.CharField(max_length=25, blank=True)
    preparacion = models.TextField()
    link_foto = models.URLField(blank=True)
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_actualizado = models.DateTimeField(default=timezone.now)
    alergenos = models.ManyToManyField(Alergeno, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Elaboraciones"