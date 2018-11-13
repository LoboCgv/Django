from django.shortcuts import render

# Create your views here.
def ListaViviendas(request):
    return render(request,"ListVivienda.html")