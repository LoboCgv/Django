from django.shortcuts import render
from django.http import HttpResponse
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
    
class ViviendaFiltro(APIView):
    def get(self,request,filtro):
        viviendas=Vivienda.objects.filter(patio=filtro)
        serializer=ViviendaSerializer(viviendas,many=True)
        return Response(serializer.data)
    def post(self,request,calle,numero,patio,habitaciones):
        v=Vivienda(calle=calle,numero=numero,habitaciones=habitaciones,patio=patio)
        v.save()
        viviendas=Vivienda.objects.all()
        serializer=ViviendaSerializer(viviendas,many=True)
        return Response(serializer.data)
