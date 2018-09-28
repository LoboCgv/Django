from django.db import models

# Create your models here.
class Comentario(models.Model):
    codigoComentario=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    correo=models.EmailField(null=True,blank=True)
    mensaje=models.TextField(max_length=5000)
    def __str__(self):
        return str(self.codigoComentario)+" "+self.nombre