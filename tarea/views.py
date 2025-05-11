from django.shortcuts import render, redirect
# Importar los modelos para interactuar con la base de datos
from .models import Tarea

# Create your views here.


# Vistas de la aplicacion
def Principal(request):
    return render(request, 'tareas/Main.html',{'tareas':Tarea.objects.all()})

def CreacionTarea(request):
    return render(request,"tareas/creacion.html")

def EditarTarea(request,id):
    tarea = Tarea.objects.get(id=id)
    return render(request,"tareas/editar.html",{'tarea':tarea})


# Logica de las funciones solicitadas
def guardarTarea(request):
    # Variable con todos los datos de las tareas
    data = {'tareas':Tarea.objects.all()}
    if request.method == "POST":
        # Crear la tarea y asignar el valor a cada atributo

        tarea = Tarea(
            titulo=request.POST["titulo"],
            descripcion=request.POST["descripcion"],
            fecha_limite=request.POST["fecha_limite"],
            prioridad=request.POST["prioridad"]
        )
        # Guardar la tarea registrada en base de datos
        tarea.save()
    # Redirigir a la pagina donde se listan las tareas enviando los datos nuevos a la tabla
    return redirect('inicio')

# eliminar una tarea
def EliminarTarea(request, id):
    # Eliminar la tarea con el id 
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    # Redirigir a la pagina donde se listan las tareas  
    return redirect('inicio')

# Confirmar la actualizacion y guardar los datos en base
def Actualizar(request):
    #Guardar l los nuevos datos en la base de datos 
    try:
        tarea = Tarea.objects.get(id=request.POST["id"])
        tarea.titulo = request.POST["titulo"]
        tarea.descripcion = request.POST["descripcion"]
        tarea.fecha_limite = request.POST["fecha_limite"]
        tarea.prioridad = request.POST["prioridad"]
        tarea.save()
    except Exception as e:
        pass 
    return redirect('inicio')