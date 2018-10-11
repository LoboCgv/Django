from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#manejo de usuarios perzonalizados
class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Agregamos datos
    perfil=models.CharField(max_length=20,default="Invitado")