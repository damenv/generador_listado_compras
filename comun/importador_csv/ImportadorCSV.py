from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import logging
from alergenos.forms import AlergenoForm
from proveedores.forms import ProveedorForm
from elaboraciones.forms import ElaboracionForm
from ingredientes.forms import IngredienteForm
from productos.forms import ProductoForm

from alergenos.models import Alergeno
from proveedores.models import Proveedor
from productos.models import Producto
from elaboraciones.models import Elaboracion



class ImportadorCSV:
    def __init__(self, modelo: str, fields: list):
        self.modelo = modelo
        self.forma_fields = fields
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def form_selector(modulo, data_dict):
        if modulo == "elaboracion":
            return ElaboracionForm(data_dict)
        elif modulo == "ingrediente":
            return IngredienteForm(data_dict)
        elif modulo == "producto":
            return ProductoForm(data_dict)
        elif modulo == "alergeno":
            return AlergenoForm(data_dict)
        elif modulo == "proveedor":
            return ProveedorForm(data_dict)

    def obtener_objeto_de_modelo(self, modelo, llave, parametros):
        parametros = parametros.split('/')
        multiples_objetos = []
        for parametro in parametros:
            parametro = parametro.strip()

            if modelo == "elaboracion":
                result = Alergeno.objects.filter(alergeno__iexact=parametro)[:1]
                if result.__len__() > 0:
                    multiples_objetos.append(result[0])

            elif modelo == "ingrediente":
                if llave == "producto":
                    result = Producto.objects.filter(producto__iexact=parametro)[:1]
                    if result.__len__() > 0:
                        return result[0]
                    else:
                        return None
                elif llave == "producto_elaboracion" or llave == "elaboracion":
                    result = Elaboracion.objects.filter(nombre__iexact=parametro)[:1]
                    if result.__len__() > 0:
                        return result[0]
                    else:
                        return None

            elif modelo == "producto":
                result = Proveedor.objects.filter(nombre__iexact=parametro)[:1]
                if result.__len__() > 0:
                    return result[0]
                else:
                    return None
        return multiples_objetos

    def upload_csv(self, request):
        data = {}
        if "POST" == request.method:
            try:
                csv_file = request.FILES["csv_file"]
                tiene_encabezado = request.POST.__contains__("encabezado")
                if not csv_file.name.endswith('.csv'):
                    messages.error(request, 'Archivo no es tipo CSV')
                    return HttpResponseRedirect(reverse(self.modelo + "-list"))
                # if file is too large, return
                if csv_file.multiple_chunks():
                    messages.error(request, "Archivo es demasiado grande (%.2f MB)." % (csv_file.size / (1000 * 1000),))
                    return HttpResponseRedirect(reverse(self.modelo + "-list"))

                file_data = csv_file.read().decode("utf-8")

                lines = file_data.split("\n")
                # loop over the lines and save them in db. If error , store as string and then display
                for line in lines:
                    if tiene_encabezado:
                        tiene_encabezado = False
                        continue

                    fields = line.split(",")
                    data_dict = {}
                    i = 0

                    for key in self.forma_fields.keys():
                        if type(self.forma_fields[key]).__name__ == "ModelChoiceField" and fields[i]:
                            data_dict[key] = self.obtener_objeto_de_modelo(self.modelo, key, fields[i])
                        elif type(self.forma_fields[key]).__name__ == "ModelMultipleChoiceField" and fields[i]:
                            data_dict[key] = self.obtener_objeto_de_modelo(self.modelo, key, fields[i])
                        else:
                            data_dict[key] = fields[i].strip()
                        i += 1

                    try:

                        form = self.form_selector(self.modelo, data_dict)
                        if form.is_valid():
                            form.save(commit=True)
                            self.logger.info("Todo bien")
                        else:
                            self.logger.error(form.errors.as_json())
                            messages.error(request, "Error al tratar de guardar la fila: " + line +
                                           "\n Errores: " + repr(form.errors))
                    except Exception as e:
                        self.logger.error(repr(e))
                        pass

            except Exception as e:
                self.logger.exception("Error al subir el archivo. " + repr(e))
                messages.error(request, "Error al subir el archivo. " + repr(e))

        return HttpResponseRedirect(reverse(self.modelo + "-list"))
