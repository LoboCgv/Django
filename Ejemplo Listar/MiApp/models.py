from django.db import models

# Create your models here.
class Persona(models.Model):
    codigoPersona=models.AutoField(primary_key=True)
    nombrePersona=models.CharField(max_length=30)
    fechaNacimiento=models.DateField()
    mayorEdad=models.BooleanField(default=False)
    numeroFono=models.BigIntegerField(null=True,blank=True)
    def __str__(self):
        return self.nombrePersona+ " "+str(self.codigoPersona)

class Mascota(models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    nombreMascota=models.CharField(max_length=20)
    def __str__(self):
        return self.nombreMascota

class MascotaPersona(models.Model):
    codigoMascota=models.ForeignKey(Mascota,on_delete=models.CASCADE)
    codigoPersona=models.ForeignKey(Persona,on_delete=models.CASCADE)