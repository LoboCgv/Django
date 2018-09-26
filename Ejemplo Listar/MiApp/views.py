from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Persona, Mascota

# Create your views here.
def index(request):
    personas=Persona.objects.all()
    plantilla=loader.get_template("ListaPersona.html")
    contexto={
        'persones':personas,
    }
    return HttpResponse(plantilla.render(contexto,request))
def contacto(request):
    return HttpResponse("Hola miunco este es el contacto")
def personaMascota(request):
    personas=Persona.objects.all()
    mascotas=Mascota.objects.all()
    plantilla=loader.get_template("otraPlantilla.html")
    contexto={
        'personas':personas,
        'mascotas':mascotas,
    }
    return HttpResponse(plantilla.render(contexto,request))