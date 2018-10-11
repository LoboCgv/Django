from django import forms

class AgregarUsuario(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")


class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")