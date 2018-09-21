from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
from django.template import loader

# Create your views here.
def index(request):
	return HttpResponse("Este es el index")
def contacto(request):
	return HttpResponse("Este es el contacto")
def detalle(request):
	return HttpResponse("este es el detalle")
def listar(request):
	persones=Persona.objects.all()
	#persones=Persona.objects.filter(nombrePersona="carlos")
	yo=Persona.objects.get(codigoPersona=1)
	plantilla=loader.get_template("ListPersonas.html")
	diccionario={
		'personas':persones,
		'yo':yo,
	}
	return HttpResponse(plantilla.render(diccionario,request))
	