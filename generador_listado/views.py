from django.shortcuts import render
# Create your views here.
from elaboraciones.models import Elaboracion
from ingredientes.models import Ingrediente
from productos.models import Producto

def convertidor_unidad_medida(origen: str, destino: str):
    print(origen)

def obtener_listado_compras(elaboracion):
    #elab = Elaboracion.objects.get(pk=elaboracion)
    # Obtener listado de ingredientes
    ingredientes_elab = Ingrediente.objects.filter(elaboracion=elaboracion)

    # Obtener el valor de cada ingrediente y respectiva unidad de medida
    total_ingredientes = 0
    monto_ingredientes = {"ingredientes": {}, "total": 0}
    for ingrediente in ingredientes_elab:
        try:
            producto = Producto.objects.get(producto=ingrediente.producto)
            precio_sin_iva = producto.precio * ingrediente.cantidad
            precio_con_iva = round(precio_sin_iva * (1+producto.iva/100.00),2)
            monto_ingredientes["ingredientes"].update({f"{producto.producto}":
                                                           { "cantidad": ingrediente.cantidad,
                                                             "precio_unitario": producto.precio,
                                                             "precio_sin_iva": precio_sin_iva,
                                                             "iva": producto.iva,
                                                             "precio_con_iva": precio_con_iva
                                                             }
                                                       })
            total_ingredientes += precio_con_iva
        except:
            ingrediente_elab = Elaboracion.objects.get(nombre=ingrediente.producto_elaboracion)
            if ingrediente_elab.id != elaboracion:
                resultado = obtener_listado_compras(ingrediente_elab.id)
                monto_ingredientes["ingredientes"].update({f"{ingrediente_elab.nombre}":
                                                               {"cantidad": ingrediente.cantidad,
                                                                "precio_unitario": resultado["total"],
                                                                "precio_sin_iva": "-",
                                                                "iva": "-",
                                                                "precio_con_iva": resultado["total"]
                                                                }
                                                           })
                total_ingredientes += resultado["total"]

    monto_ingredientes["total"] = total_ingredientes
    return monto_ingredientes

def resultados(request, elaboracion):
    response = obtener_listado_compras(elaboracion)
    return render(request, 'generador_listado/hoja_resultados.html', response)