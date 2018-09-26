from django.contrib import admin
from .models import Persona, Mascota, MascotaPersona
# Register your models here.

admin.site.register(Persona)
admin.site.register(Mascota)
admin.site.register(MascotaPersona)