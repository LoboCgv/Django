from django import forms
from .models import Cliente

class AgregarClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=('nombreCliente','rutCliente',)