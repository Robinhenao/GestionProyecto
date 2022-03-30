from pickle import TRUE
from tabnanny import verbose
from django.db import models

# Create your models here.

class Proyectos(models.Model):
    estados = (('F','Finalizado'),('P','En ejecucion'))
    nombre = models.CharField()
    objetivo_general = models.CharField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    director = models.CharField()
    presupuesto = models.CharField()
    porcentaje_avance = models.IntegerField()
    estado = models.CharField(max_length=1, choices=estados)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        db_table= 'proyectos'
        verbose_name= 'Proyecto'
        verbose_name_plural='Proyectos'
        ordering=['-id']
   
    

     

class Estudiantes(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    numero_id = models.IntegerField(primary_key=True)
    telefono = models.CharField(max_length=12)
    carrera = models.CharField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table= 'estudiantes'
        verbose_name= 'Estudiante'
        verbose_name_plural='Estudiantes'
        ordering=['-id']
   
    
    
class Objetivos_espesificos(models.Model):
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    contenido = models.CharField()

    class Meta:
        db_table= 'objetivos_espesificos'
        verbose_name= 'Objetivo espesifico'
        verbose_name_plural='Objetivos espesificos'
        ordering=['-id']

    def __str__(self) -> str:
        return super().__str__()

    

