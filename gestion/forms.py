from django import forms
from .models import Estudiante
from .models import Proyecto


class FormStudent(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre','apellido','numero_id','telefono','carrera','proyecto','fecha_ingreso')

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre','objetivo_general','fecha_inicio','fecha_fin','director','presupuesto','porcentaje_avance','estado')