from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('index',views.index),
    path('contacto',views.contacto),
    path('personasMascota',views.personaMascota),
]