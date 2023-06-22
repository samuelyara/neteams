from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    rol = models.CharField(max_length=50)
    # Aquí se define el argumento related_name para evitar el conflicto
    groups = models.ManyToManyField(Group, related_name='usuario_set')
    user_permissions = models.ManyToManyField(Permission, related_name='usuario_set')

