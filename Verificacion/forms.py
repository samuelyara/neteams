from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    ROLES = (
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
    )

    rol = forms.ChoiceField(choices=ROLES)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'rol')

