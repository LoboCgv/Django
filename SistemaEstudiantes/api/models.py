
from django.db import models

class Alumno(models.Model):
    Femenino = 'F'
    Masculino = 'M'
    choices = ((Femenino, 'Femenino'), (Masculino, 'Masculino'))

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.IntegerField()
    genero = models.CharField(max_length=1, choices=choices, default=Femenino)