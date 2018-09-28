from django.shortcuts import render, render_to_response
from .forms import Contacto
from .models import Mensaje

# Create your views here.
def contacto(request):
    #form=Contacto()
    msgs=Mensaje.objects.all()
    form=Contacto(request.POST or None)
    variables={
        'form':form,
        'msgs':msgs,
    }
    if form.is_valid():
        datos=form.cleaned_data
        nombreIn=datos.get("nombre")
        emailIn=datos.get("email")
        mensajeIn=datos.get("mensaje")
        dbReg=Mensaje(nombre=nombreIn,correo=emailIn,mensaje=mensajeIn)
        dbReg.save()
        
    #return render_to_response("contacto.html",{'form':form})
    return render(request,"contacto.html",variables)