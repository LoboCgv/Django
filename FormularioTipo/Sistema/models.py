from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombreUsuario=models.CharField(max_length=15,primary_key=True)
    passwd=models.CharField(max_length=10)
    perfil=models.CharField(max_length=20,default="Usuario")