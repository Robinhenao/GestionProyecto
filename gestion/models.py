from pickle import TRUE
from django.db import models

# Create your models here.

class Proyecto(models.Model):
    estados = (('F','Finalizado'),('P','En ejecucion'))
    nombre = models.CharField()
    objetivo_general = models.CharField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    director = models.CharField()
    presupuesto = models.CharField()
    porcentaje_avance = models.IntegerField()
    estado = models.CharField(max_length=1, choices=estados)

     

class Estudiante(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    numero_id = models.IntegerField(primary_key=TRUE)
    telefono = models.CharField(max_length=12)
    carrera = models.CharField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    



class Objetivos_espesificos(models.Model):
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    contenido = models.CharField()


    

