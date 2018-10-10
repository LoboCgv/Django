from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^Producto/$',views.homeProducto,name="homeProducto"),
    url(r'^verStock/$',views.verStock,name="existe"),
]