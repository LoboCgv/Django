from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index,name="inicio"),
    url(r'^Usuarios/$',views.gestionarUsuarios,name="gestionarUsuarios"),
    url(r'^login/$',views.ingresar,name="login"),
    url(r'^salir/$',views.salir,name="logout"),
    ]