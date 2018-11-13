from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.ViviendaView.as_view()),
    url(r'^filtro/(?P<filtro>[a-zA-Z]+)$',views.ViviendaFiltro.as_view()),
    url(r'^add/$',views.ViviendaFiltro.as_view()),
]