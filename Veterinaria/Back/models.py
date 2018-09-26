from django.db import models

# Create your models here.
class Cliente(models.Model):
    codigoCliete=models.AutoField(primary_key=True)
    nombreCliente=models.CharField(max_length=50)
    rutCliente=models.CharField(max_length=15)
    def __str__(self):
        return (self.nombreCliente)