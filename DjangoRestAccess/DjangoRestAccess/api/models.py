from django.db import models

# Create your models here.
class Vivienda(models.Model):
    calle=models.CharField(max_length=40)
    numero=models.IntegerField()
    habitaciones=models.IntegerField()
    patio=models.BooleanField(default=False)