from django.shortcuts import render, redirect
from Tareas.models import Tarea

# Create your views here.


def panel_empleado(request):
    username = request.session.get('username')
    tarea = Tarea.objects.raw(f"SELECT * FROM Tareas_tarea WHERE completado = 0 AND empleado_id = (SELECT id FROM Verificacion_usuario WHERE username = '{username}') ORDER BY plazo_maximo ASC")
    tareaNoRealizada = Tarea.objects.raw(f"SELECT * FROM Tareas_tarea WHERE completado = 1 AND empleado_id = (SELECT id FROM Verificacion_usuario WHERE username = '{username}') ORDER BY plazo_maximo ASC")
    return render(request, 'panel_empleado.html', {'username': username, 'tareas':tarea, 'notareas':tareaNoRealizada})

def marcar_completado(request, id):
    tareas=Tarea.objects.get(id=id)
    tareas.completado=True
    tareas.save()
    return redirect('gestion_empleado')
