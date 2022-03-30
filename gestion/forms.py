from django import forms
from .models import Estudiante

class FormStudent(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre','apellido','numero_id','telefono','carrera','proyecto','fecha_ingreso')