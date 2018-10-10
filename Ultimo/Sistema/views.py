from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import Producto
from .forms import AgregarProducto

# Create your views here.
def homeProducto(request):
    form=AgregarProducto(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Producto(nombreProducto=data.get("nombreProducto"),precioProducto=data.get("precioProducto"),stock=data.get("stock"))
        regDB.save()
    form=AgregarProducto()
    productos=Producto.objects.all()
    titulo="Gestion Productos"
    return render(request,"homeProducto.html",{'productos':productos,'form':form,'titulo':titulo,})

def verStock(request):
    productos=Producto.objects.exclude(stock=0).order_by("precioProducto")
    return render(request,"verStock.html",{'productos':productos,})