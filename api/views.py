from django.shortcuts import render
from rest_framework import viewsets
from domotica.models import Habitacion, Dispositivo, Usuario, RegistroActividad
from api.serializers import HabitacionSerializer, DispositivoSerializer, UsuarioSerializer, RegistroActividadSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class HabitacionView(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class DispositivoView(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = UsuarioSerializer

class RegistroActividadView(viewsets.ModelViewSet):
    queryset = RegistroActividad.objects.all()
    serializer_class = RegistroActividadSerializer

@api_view(['GET'])
def habitaciones_list(request):
    habitaciones = Habitacion.objects.all()
    serializer = HabitacionSerializer(habitaciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def habitacion_detail(request, habitacion_id):
    habitacion = Habitacion.objects.get(id=habitacion_id)
    serializer = HabitacionSerializer(habitacion)
    return Response(serializer.data)