from django.urls import path
from .views import panel_empleado, marcar_completado

urlpatterns = [
    path('', panel_empleado, name="gestion_empleado"),
    path('marcar_completado/<int:id>/', marcar_completado, name='marcar_completado'),
]
