from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Platillos(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(default=' ', max_length=1000)
    precio = models.PositiveSmallIntegerField()
    categoria = models.PositiveSmallIntegerField()
    imagen = models.CharField(default=' ', max_length=1000)

class Tickets(models.Model):
    id_ticket = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=200)
    precio = models.PositiveSmallIntegerField()
    cantidad = models.PositiveSmallIntegerField()

class Responsables(models.Model):
    usuarioR = models.CharField(max_length=200)
    contraseñaR = models.CharField(max_length=200)
    codigoR = models.CharField(max_length=200)

class MesaInfo(models.Model):
    Mesa = models.CharField(max_length=200)
    NoMesa = models.CharField(max_length=200)
    Contraseña = models.CharField(max_length=200)
    Ubicacion = models.CharField(max_length=200)