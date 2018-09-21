from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('detalle', views.detalle, name='detalle'),
    path('contacto', views.contacto, name='contacto'),
    path('lista',views.listaPersonas,name='las personas'),
]