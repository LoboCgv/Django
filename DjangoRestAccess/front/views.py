from django.shortcuts import render

# Create your views here.
def ListaViviendas(request):
    return render(request,"ListVivienda.html")

def AgregarVivienda(request):
    return render(request,"CrearVivienda.html")