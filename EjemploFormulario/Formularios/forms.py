from django import forms

class Contacto(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput(),required=True)
    email=forms.EmailField(widget=forms.TextInput())
    mensaje=forms.CharField(widget=forms.Textarea(),required=True)
    #nombre email y mensaje son los nombres de los campos de datos