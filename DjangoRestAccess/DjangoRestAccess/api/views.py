from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vivienda
from .serializers import ViviendaSerializer
# Create your views here.
class ViviendaView(APIView):
    def get(self,request):
        viviendas=Vivienda.objects.all()
        serializer=ViviendaSerializer(viviendas,many=True)
        return Response(serializer.data)