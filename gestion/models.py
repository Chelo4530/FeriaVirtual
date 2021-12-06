from django.db import models

# Create your models here.

class Administradores(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    usuario = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=8)

