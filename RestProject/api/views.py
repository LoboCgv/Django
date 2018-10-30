from rest_framework import generics

from apiLibros import models
from . import serializers


class ListLibro(generics.ListCreateAPIView):
    queryset = models.Libro.objects.all()
    serializer_class = serializers.LibroSerializer


class DetailLibro(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Libro.objects.all()
    serializer_class = serializers.LibroSerializer