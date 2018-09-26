from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Cliente
from .forms import AgregarClienteForm


# Create your views here.
def index(request):
    clientes=Cliente.objects.all()
    salida=loader.get_template("index.html")
    contexto={
        'clientes':clientes
    }
    return HttpResponse(salida.render(contexto,request))
def ingresar(request):
    if request.method == "POST":
            form = AgregarClienteForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.nombreCliente = request.Cliente.nombreCliente
                post.rutCliente=request.rutCliente
                post.save()
                return redirect('verCliente',codigoCliente=post.codigoCliente)
                
    else:
        form = AgregarClienteForm()
    return render(request, 'ingresarCliente.html', {'form': form})
    
def verCliente(request,codigoCliente):
    client=Cliente.objects.get(codigoCliete=codigoCliente)
    salida=loader.get_template("ingresarCliente.html")
    context={
        'cliente':client
    }
    return HttpResponse(salida.render(context,request))