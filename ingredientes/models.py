from django.db import models
from productos.models import Producto
from elaboraciones.models import Elaboracion


class Ingrediente(models.Model):
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE, blank=True, null=True)
    producto_elaboracion = models.ForeignKey('elaboraciones.Elaboracion', on_delete=models.CASCADE, related_name = "elaboracion_como_ingrediente", blank=True, null=True)
    elaboracion = models.ForeignKey('elaboraciones.Elaboracion', on_delete=models.CASCADE,)
    cantidad = models.FloatField(default=0)

    def __str__(self):
        if self.producto is None:
            return self.producto_elaboracion
        else:
            return self.producto

    class Meta:
        verbose_name_plural = "Ingredientes"