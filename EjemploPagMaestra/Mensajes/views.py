from django.shortcuts import render
from .models import Comentario
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    comentarios=Comentario.objects.all()
    plantilla=loader.get_template("index.html")
    titulo="Este es el index"
    contexto={
        'comentarios':comentarios,
        'titulo':titulo,
    }
    return HttpResponse(plantilla.render(contexto,request))
def mensaje(request):
    return HttpResponse("Comentarios")
def otro(request):
    titulo="Este es el otro"
    plantilla=loader.get_template("otro.html")
    contexto={
        'titulo':titulo,
    }
    return HttpResponse(plantilla.render(contexto,request))