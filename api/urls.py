from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register(r'habitaciones', HabitacionView)
router.register(r'dispositivos', DispositivoView)
router.register(r'usuarios', UsuarioView)
router.register(r'registros', RegistroActividadView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title="Usuarios API")),
    path('api/usuarios/<int:id>', views.UsuarioView.as_view({'get': 'retrieve'})),
     path('habitaciones/', habitaciones_list, name='habitaciones_list'),
    path('habitaciones/<int:habitacion_id>/', habitacion_detail, name='habitacion_detail'),
]