from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListLibro.as_view()),
    path('<int:pk>/', views.DetailLibro.as_view()),
]