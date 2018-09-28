from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns=[
    url(r'^mensaje/$',views.mensaje),
   
    url(r'^index/$',views.index),
    url(r'^otro$',views.otro,name='otro'),
   
]