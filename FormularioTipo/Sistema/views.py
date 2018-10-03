from django.shortcuts import render, render_to_response
from .models import Usuario
from django.template import loader
from django.http import HttpResponse
from .forms import AgregarUsuario

# Create your views here.
def index(request):
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"Pagina Inicial",
        
    }
    return HttpResponse(plantilla.render(contexto,request))

def gestionUsuario(request):
    #idea es tener un formulario y una lista de usuarios pero sólo con perfil de administrador
    #crear la lista de usuarios
    form=AgregarUsuario(request.POST or None)
    usuarios=Usuario.objects.all()
    #crear la plantilla
    plantilla=loader.get_template("gestionUsuario.html")
    #contexto de variables
    
    if form.is_valid():
        datos=form.cleaned_data
        nombreUsuario=datos.get("nombreUsuario")
        passwd=datos.get("passwd")
        perfil=datos.get("perfil")
        regdb=Usuario(nombreUsuario=nombreUsuario,passwd=passwd,perfil=perfil)
        regdb.save()
    
    #enviar datos
    #return HttpResponse(plantilla.render(contexto,request))
    
    contexto={
        'usuarios':usuarios,
        'form':form,
    }
    
    return render(request,"gestionUsuario.html",contexto)
def logout(request):
    try:
        del request.session['nombreUsuario']
    except KeyError:
        pass
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"Salio",
    }
    return HttpResponse(plantilla.render(contexto,request))

def modificarUsuario(request,pk):
    usuario=Usuario.objects.get(nombreUsuario=pk)
    form=AgregarUsuario(request.POST or None)
    
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':usuario,
        
    }
    return HttpResponse(plantilla.render(contexto,request))
    