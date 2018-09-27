from django.db import models

# Create your models here.
class Persona(models.Model):
    codigoPersona=models.AutoField(primary_key=True)
    nombrePersona=models.CharField(max_length=20)
    def __str__(self):
        return self.nombreUsuario