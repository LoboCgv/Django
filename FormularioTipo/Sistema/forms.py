from django import forms
tipos=(
    ('Administrador','Administrador'),
    ('Invitado','Invitado'),
    ('Supervisor','Supervisor')
)
class AgregarUsuario(forms.Form):
    nombreUsuario=forms.CharField(widget=forms.TextInput(),required=True,label="Nombre Usuario")
    passwd=forms.CharField(widget=forms.PasswordInput(),required=True,label="Contraseña")
    #perfil=forms.MultipleChoiceField(
     #   widget=forms.CheckboxSelectMultiple,choices=tipos,
    #)
    perfil=forms.ChoiceField(choices=tipos)
    