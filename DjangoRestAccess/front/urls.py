from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.ListaViviendas),
    url(r'^agregar/$',views.AgregarVivienda)
]