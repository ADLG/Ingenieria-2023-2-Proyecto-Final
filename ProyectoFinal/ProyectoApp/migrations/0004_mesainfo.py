# Generated by Django 4.1.6 on 2023-06-01 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoApp', '0003_responsables'),
    ]

    operations = [
        migrations.CreateModel(
            name='MesaInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mesa', models.CharField(max_length=200)),
                ('NoMesa', models.CharField(max_length=200)),
                ('Contraseña', models.CharField(max_length=200)),
                ('Ubicacion', models.CharField(max_length=200)),
            ],
        ),
    ]
