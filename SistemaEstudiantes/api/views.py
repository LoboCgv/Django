from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Alumno
from .serializers import AlumnoSerializer

class Get_Alumno_List(APIView):
    def get(self, request):
        students = Alumno.objects.all()
        serialized = AlumnoSerializer(students, many=True)
        return Response(serialized.data)

def homepage(request):
    return render(request, 'index.html')