# generador_listado_compras
 Proyecto de python encargado de generar un listado de compras a partir de un listado de elaboraciones

## Importador de Archivos CSV

### Alergenos

| Columnas | Tipo de Dato | Obligatorio |
| -------- | ------------ |-------------|
| alergeno | Cadena de caracteres | si |

### Elaboraciones

| Columnas                 | Tipo de Dato                         | Obligatorio |
|--------------------------|--------------------------------------|-------------|
| nombre                   | Cadena de caracteres                 | si |
| tamaño de racion         | Decimal                              | si |
| numero de raciones       | Decimal                              | si |
| tiempo de produccion (h) | Decimal                              | si |
| familia                  | Cadena de caracteres                 | no |
| formato                  | Cadena de caracteres                 | no |
| sabor                    | Cadena de caracteres                 | no |
| producto base            | Cadena de Caracteres                 | no |
| preparacion              | Cadena de Caracteres                 | si |
| link a foto              | URL                                  | no |
| alergenos                | Cadena de Caracteres separados por / | no |

### Ingredientes

| Columnas | Tipo de Dato | Obligatorio |
|----------| ------------ |-------------|
| producto | Cadena de caracteres | no          |
| producto_elaboracion | Cadena de caracteres | no       |
| elaboracion | Cadena de caracteres | si |
| cantidad | Decimal | si |

### Productos

| Columnas | Tipo de Dato         | Obligatorio |
|----------|----------------------|-------------|
| producto | Cadena de caracteres | si          |
| precio   | Decimal              | si          |
| iva      | Decimal              | si          |
| cantidad | Decimal              | si          |
| unidad de medida | Caracter (u,g,kg,l) | si |
| proveedor | Cadena de caracteres | no |

### Proveedor

| Columnas             | Tipo de Dato                                         | Obligatorio |
|----------------------|------------------------------------------------------|-------------|
| nombre               | Cadena de caracteres                                 | si          |
| familia de productos | Cadena de caracteres                                 | si          |
| direccion            | Cadena de caracteres                                 | no          |
| pedido minimo        | Decimal                                              | si          |
| telefono             | Caracteres en el formato en el formato: '+999999999' | no          |
| correo electronico   | Cadena de caracteres en formato correo@dominio.dom   | no          |