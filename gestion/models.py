from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

class Proyecto(models.Model):
    estados = (('F','Finalizado'),('E','En ejecucion'))
    nombre = models.CharField(max_length=100)
    objetivo_general = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    director = models.ForeignKey(User, on_delete=models.CASCADE)
    presupuesto = models.CharField(max_length=100)
    porcentaje_avance = models.IntegerField(null = True)
    estado = models.CharField(max_length=1, choices=estados)

    def __str__(self):
        return self.nombre

    class meta:
        db_table= 'proyecto'
        verbose_name= 'Proyecto'
        verbose_name_plural='Proyectos'
        ordering=['id']
  

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_id = models.IntegerField(primary_key=True)
    telefono = models.CharField(max_length=12)
    carrera = models.CharField(max_length=100)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()

    def __str__(self) -> str:
        return super().__str__()
    
    class meta:
        db_table= 'estudiante'
        verbose_name= 'Estudiante'
        verbose_name_plural='Estudiantes'
        ordering=['id']
   
    
    
class Objetivos_especificos(models.Model):
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE,null=True)
    contenido = models.CharField(max_length=100)
    estado = models.BooleanField(null=True,verbose_name="Efectuado")

    def __str__(self) -> str:
        return super().__str__()

    class meta:
        db_table= 'objetivos_especificos'
        verbose_name= 'Objetivo especifico'
        verbose_name_plural='Objetivos especificos'
        ordering=['id']

    

    

