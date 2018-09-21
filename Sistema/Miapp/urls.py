from django.urls import path
from . import views
urlpatterns=[
	path('',views.index),
	path('detalle',views.detalle),
	path('contacto',views.contacto),
	path('listar',views.listar),
]