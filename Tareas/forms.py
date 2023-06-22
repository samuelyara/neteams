from django import forms
from .models import Tarea
from Verificacion.models import Usuario

class TareaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        self.fields['empleado'].queryset = Usuario.objects.filter(rol='empleado')
    
    class Meta:
        model = Tarea
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de la tarea',
            'descripcion': 'Descripción de la tarea',
            'plazo_maximo': 'Plazo máximo para la tarea',
            'empleado': 'Empleado asignado a la tarea',
        }
        exclude = ('completado',)

        widgets = {
            'plazo_maximo': forms.DateInput(attrs={'type': 'date'}),
        }