from rest_framework import serializers
from .models import Vivienda
class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            '__all__'
        )
        model=Vivienda
    