from django import forms
from django.forms import ModelForm
from .models import Estudiante
from .models import Proyecto
from .models import Objetivos_especificos

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class FormStudent(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre','apellido','numero_id','telefono','fecha_ingreso','carrera',)
        widgets={'fecha_ingreso':DatePickerInput(),}

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre','objetivo_general','fecha_inicio','fecha_fin','presupuesto')
        widgets={'fecha_inicio':DatePickerInput(),'fecha_fin':DatePickerInput(),}

class FormObjetivosEspecificos(forms.ModelForm):
    class Meta:
        model = Objetivos_especificos
        fields = ('contenido','estado') 