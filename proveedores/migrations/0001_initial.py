# Generated by Django 4.0.2 on 2022-05-03 12:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('familia_productos', models.CharField(max_length=75)),
                ('direccion', models.CharField(blank=True, max_length=100)),
                ('pedido_minimo', models.FloatField(default=0.0)),
                ('telefono', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Telefono debe introducirse en el formato: '+999999999'. Se aceptan hasta 15 dígitos.", regex='^\\+?1?\\d{9,15}$')])),
                ('correo_electronico', models.CharField(blank=True, max_length=254, validators=[django.core.validators.EmailValidator(message='Introducir un correo válido')])),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
