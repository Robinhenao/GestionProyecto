from django import forms
from .models import Estudiante
from .models import Proyecto
from .models import Objetivos_especificos


class FormStudent(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre','apellido','numero_id','telefono','carrera','fecha_ingreso')

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre','objetivo_general','fecha_inicio','fecha_fin','director','presupuesto')

class FormObjetivosEspecificos(forms.ModelForm):
    class Meta:
        model = Objetivos_especificos
        fields = ('contenido','estado') 