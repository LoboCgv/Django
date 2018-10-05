from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from .models import Mascota
from .forms import AgregarMascota, AgregarCliente
# Create your views here.

def gestionCliente(request):
    
    form=AgregarCliente(request.POST or None)
    if form.is_valid():
        datos=form.cleaned_data
        regDb=Cliente(nombreCliente=datos.get("nombreCliente"),apellidoCliente=datos.get("apellidoCliente"))
        regDb.save()
    clientes=Cliente.objects.all()
    contexto={
        'clientes':clientes,
        'form':form,
    }
    return render (request,"gestionCliente.html",contexto)

def gestionMascota(request):
    form=AgregarMascota(request.POST or None)
    if form.is_valid():
        datos=form.cleaned_data
        regDb=Mascota(nombreMascota=datos.get("nombreMascota"))
        regDb.save()
    mascotas=Mascota.objects.all()
    contexto={
        'mascotas':mascotas,
        'form':form,
    }
    return render (request,"gestionMascota.html",contexto)

def verCliente(request,pk):
    cliente=Cliente.objects.get(codigoCliente=pk)
    return render(request,"verCliente.html",{'cliente':cliente})
def verMascota(request,pk):
    mascota=Mascota.objects.get(codigoMascota=pk)
    return render(request,"verMascota.html",{'mascota':mascota})

