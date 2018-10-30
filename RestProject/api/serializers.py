from rest_framework import serializers
from apiLibros import models


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Libro