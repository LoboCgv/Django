from django.db import models

# Create your models here.
class Persona(models.Model):
	codigoPersona=models.AutoField(primary_key=True)
	nombrePersona=models.CharField(max_length=30)
	emailPersona=models.EmailField(default="sincorreo@gmail.com")
	direccion=models.TextField(null=True, blank=True)
	def __str__(self):
		return self.nombrePersona