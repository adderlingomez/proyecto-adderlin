# Generated by Django 5.0.3 on 2024-04-25 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apostadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apostador', models.CharField(max_length=100)),
                ('detalles', models.CharField(max_length=100)),
                ('tu_tiempo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo electronico')),
            ],
        ),
        migrations.CreateModel(
            name='Caracteristica_apostadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_juegos', models.IntegerField(default=False)),
                ('veces_perdi', models.IntegerField()),
                ('juegos', models.CharField(max_length=100)),
                ('apostador', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='project_final.apostadores')),
            ],
        ),
    ]
