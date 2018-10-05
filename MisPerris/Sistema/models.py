from django.db import models

# Create your models here.
class Cliente(models.Model):
    codigoCliente=models.AutoField(primary_key=True)
    nombreCliente=models.CharField(max_length=20)
    apellidoCliente=models.CharField(max_length=20)
    def dibujarCliente(self):
        return self.nombreCliente+" "+self.apellidoCliente

class Mascota(models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    nombreMascota=models.CharField(max_length=20)

class MascotaCliente(models.Model):
    codigoMascota=models.ForeignKey(Mascota,on_delete=models.CASCADE)
    codigoCliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)