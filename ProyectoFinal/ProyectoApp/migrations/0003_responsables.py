# Generated by Django 4.1.6 on 2023-05-31 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoApp', '0002_tickets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarioR', models.CharField(max_length=200)),
                ('contraseñaR', models.CharField(max_length=200)),
                ('codigoR', models.CharField(max_length=200)),
            ],
        ),
    ]
