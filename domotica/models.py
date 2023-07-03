from django.db import models

# Create your models here.
class Habitacion(models.Model):
    nombre = models.CharField(max_length=100)
    dispositivos = models.ManyToManyField('Dispositivo', blank=True, related_name='habitaciones_rel')

    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='dispositivos_rel')
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    correo = models.EmailField()
    clave = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario

class RegistroActividad(models.Model):
    fecha_hora_registro = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ACCIONES = [
        ('encendido', 'Encendido'),
        ('apagado', 'Apagado'),
        ('ajuste_temperatura', 'Ajuste de temperatura'),
    ]
    accion_realizada = models.CharField(max_length=50, choices=ACCIONES)

    def __str__(self):
        return f'Registro {self.id}'