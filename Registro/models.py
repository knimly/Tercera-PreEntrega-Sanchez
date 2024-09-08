from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre= models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.EmailField()

    
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)

class Entrega(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    entregado = models.BooleanField()


    