from django.urls import path
from Main import views as Mainv

urlpatterns = [
    path('', Mainv.inicio, name="inicio"),
]
