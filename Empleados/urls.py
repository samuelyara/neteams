from django.urls import path
from .views import panel_administrador, eliminar_tarea, editar_tarea

urlpatterns = [
    path('', panel_administrador, name="gestion_administrador"),
    path('eliminar_tarea/<int:id>/', eliminar_tarea, name='eliminar_tarea'),
    path('editar_tarea/<int:id>/', editar_tarea, name='editar_tarea')
]
