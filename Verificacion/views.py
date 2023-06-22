from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

from Verificacion.models import Usuario
from .forms import RegistroForm

class VRegistro(View):
    def get(self, request):
        if request.user.is_authenticated:
            rol = request.user.rol  # Obtener rol del usuario logueado
            if rol == 'admin':
                return redirect('gestion_administrador')
            elif rol == 'empleado':
                return redirect('gestion_empleado')
            else:
                logout(request)
                return redirect('inicio')
        else:
            form = RegistroForm()
            return render(request, 'registro/registro.html', {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'registro/registro.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


def ingresar(request):
    if request.user.is_authenticated:
        rol = request.user.rol  # Obtener rol del usuario logueado
        if rol == 'admin':
            return redirect('gestion_administrador')
        elif rol == 'empleado':
            return redirect('gestion_empleado')
        else:
            logout(request)
            return redirect('inicio')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                nombre_usuario = form.cleaned_data.get('username')
                contraseña_usuario = form.cleaned_data.get('password')
                usuario = authenticate(username=nombre_usuario, password=contraseña_usuario)
                if usuario is not None:
                    login(request, usuario)
                    request.session['username'] = usuario.username
                    request.session['rol'] = usuario.rol
                    rol = usuario.rol
                    if rol == 'admin':
                        return redirect('gestion_administrador')
                    elif rol == 'empleado':
                        return redirect('gestion_empleado')
            else:
                return render(request, 'ingresar/ingresar.html', {'form': form})
        form = AuthenticationForm()
        return render(request, 'ingresar/ingresar.html', {'form': form})
