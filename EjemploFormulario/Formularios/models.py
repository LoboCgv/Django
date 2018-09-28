from django.db import models

# Create your models here.
class Mensaje(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    correo=models.CharField(max_length=20,null=True,blank=True)
    mensaje=models.TextField(max_length=200)