from django.shortcuts import render, render_to_response
from .models import Persona
from django.template import loader,RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactoForm
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    personas=Persona.objects.all()
    plantilla=loader.get_template("index.html")
    contexto={
        'personas':personas,
    }
    return HttpResponse(plantilla.render(contexto,request))

def contacto(request):
    if request.method=='POST':
        formulario=ContactoForm(request.POST)
        if formulario.is_valid():
            titulo="Titulo del mensaje o asunto"
            contenido=formulario.cleaned_data['mensaje']+"\n"
            contenido+="comunicarse a "+formulario.cleaned_data['correo']
            correo=EmailMessage(titulo,contenido,to=['carlosr.gonzalezv@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario=ContactoForm()
    return render_to_response('contacto.html',{'formulario':formulario,})