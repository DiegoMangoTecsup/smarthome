from django.shortcuts import render
from rest_framework import serializers
from domotica.models import Habitacion, Dispositivo, Usuario, RegistroActividad



class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'


class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class RegistroActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroActividad
        fields = '__all__'