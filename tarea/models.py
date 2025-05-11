from django.db import models

# Create your models here.
class Tarea(models.Model):
    class Meta:
        db_table = "Tareas"


    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_limite = models.DateField()
    prioridad = models.CharField(max_length=50)
    
