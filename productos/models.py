from django.db import models
from comun.unidades_medida.unidadesMedida import unidadesMedida


class Producto(models.Model):

    producto = models.CharField(max_length=75)
    precio = models.FloatField(default=0)
    iva = models.FloatField(default=10.0)
    cantidad = models.FloatField(default=1)
    unidad_medida = models.CharField(max_length=10,
                                     choices=unidadesMedida.choices,
                                     default=unidadesMedida.UNIDAD)
    proveedor = models.ForeignKey('proveedores.Proveedor', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.producto

    class Meta:
        verbose_name_plural = "Productos"