from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^clientes/$',views.gestionCliente,name="gestionCliente"),
    url(r'^mascotas/$',views.gestionMascota,name="gestionMascota"),
    url(r'^clientes/(?P<pk>[0-9])/$',views.verCliente,name="verCliente"),
    url(r'^mascotas/(?P<pk>[0-9])/$',views.verMascota,name="verMascota"),
]