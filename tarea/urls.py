from django.urls import path
from .views import *

# Urls de tareas
urlpatterns = [
    #rutas de vistas
    path("",Principal,name="inicio"),
    path("creacion/",CreacionTarea,name="creacionTarea"),
    path("editar/<int:id>",EditarTarea,name="editar"),
    # Rutas de logica
    path("creacion/guardar",guardarTarea,name="saveWork"),
    path("eliminar/<int:id>",EliminarTarea,name="eliminar"),
    path("editar/guardar",Actualizar,name="actualizarTarea")
]

# Urls de la aplicacion para el modulo de tareas
