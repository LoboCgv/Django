from django.db import models

# Create your models here.
class Producto(models.Model):
    codigoProducto=models.AutoField(primary_key=True)
    nombreProducto=models.CharField(max_length=30)
    precioProducto=models.IntegerField()
    stock=models.IntegerField(default=0)
