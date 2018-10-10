from django import forms

class AgregarProducto(forms.Form):
    nombreProducto=forms.CharField(widget=forms.TextInput(),label="Nombre Producto")
    precioProducto=forms.IntegerField(widget=forms.TextInput(),label="Precio Producto")
    stock=forms.IntegerField(widget=forms.TextInput(),label="Stock Producto")