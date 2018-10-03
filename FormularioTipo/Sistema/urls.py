from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index, name="inicio"),
    url(r'gestionUsuario',views.gestionUsuario,name="gestionUsuario"),
    url(r'logout',views.logout,name="logout"),
    url(r'^modificarUsuario/(?P<pk>[a-zA-Z0-9_]+)/$',views.modificarUsuario,name="modificarUsuario")
]