from django import forms

class AgregarCliente(forms.Form):
    nombreCliente=forms.CharField(widget=forms.TextInput(),label="Nombre Cliente")
    apellidoCliente=forms.CharField(widget=forms.TextInput(),label="Apellido Cliente")  
class AgregarMascota(forms.Form):
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre Mascota") 