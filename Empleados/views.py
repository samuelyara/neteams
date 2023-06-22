from django.shortcuts import render, redirect
from Tareas.forms import TareaForm
from Tareas.models import Tarea

def panel_administrador(request):
    username = request.session.get('username')
    tarea_form = TareaForm(request.POST or None)
    tarea = Tarea.objects.all()
    
    if request.method == 'POST':
        if tarea_form.is_valid():
            tarea = tarea_form.save(commit=False)
            # Aquí puedes realizar cualquier acción adicional con la tarea antes de guardarla en la base de datos
            tarea.save()
            return redirect('gestion_administrador')  # Redirige a la página que deseas después de guardar la tarea
    
    return render(request, 'panel_administrador.html', {'username': username, 'tarea_form': tarea_form, 'tareas':tarea})


def eliminar_tarea(request, id):
    tarea=Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('gestion_administrador')

def editar_tarea(request, id):
    tarea = Tarea.objects.get(id=id)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('gestion_administrador')
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'administrador/editar_tarea.html', {'form': form})

