from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Persona
# Create your views here.

def index(request):
    return HttpResponse("Este es el index")

def detalle(request):
    return HttpResponse("Este es el detalle")

def contacto(request):
    return HttpResponse("Este es el contacto")
    
def listaPersonas(request):
    personas=Persona.objects.all()
    template=loader.get_template('VerPersona.html')
    context={
        'personas':personas,
    }
    return HttpResponse(template.render(context,request))