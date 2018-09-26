from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('ingresar',views.ingresar),
    path('verCliente/<int:codigoCliente>/',views.verCliente),
    ]