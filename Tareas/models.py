from django.db import models
from Verificacion.models import Usuario

# Create your models here.


class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=400)
    plazo_maximo = models.DateField()
    completado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    empleado = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.descripcion