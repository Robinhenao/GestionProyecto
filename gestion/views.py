import re
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from gestion.forms import FormStudent
from gestion.forms import FormProyecto
from gestion.forms import FormObjetivosEspecificos
from gestion.forms import FormProyecto, FormStudent
from gestion.models import Estudiante, Objetivos_especificos, Proyecto
from django.core.paginator import Paginator
from django.contrib import messages


def calacular_porcentaje_avance(project_id):
    targets = Objetivos_especificos.objects.filter(proyecto = project_id)
    contador_true = 0
    No_objetivos = 0
    
    for target in targets:
        No_objetivos = No_objetivos + 1
        if target.estado == True:
            contador_true = contador_true + 1
    if No_objetivos>0:
        porcentaje = 100 / No_objetivos
        porcentaje_avance = int(contador_true * porcentaje)
        return  porcentaje_avance
    
    return 0
        


@login_required(login_url='login')
def gestion(request):
    listado_posts =Proyecto.objects.filter(director=request.user.id)
    paginator = Paginator(listado_posts, 6)
    pagina = request.GET.get("page") or 1
    posts = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, posts.paginator.num_pages + 1)
    return render(request, "gestion_proyecto.html",{"projects":posts,"paginas": paginas, "pagina_actual": pagina_actual })


def manage_students(request, project_id):
    if request.method == "POST":
        idid = Proyecto.objects.get(pk=project_id)
        form=FormStudent(request.POST,request.FILES)
        if form.is_valid():
            estudiante= form.save(commit=False)
            estudiante.proyecto=idid
            estudiante.save()
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
    form=FormStudent() 
    students = Estudiante.objects.filter(proyecto = project_id)
    return render(request, "manage_students.html", {"form": form,"students":students,'project_id':project_id})


def admin_project(request,project_id):
    project = Proyecto.objects.get(id =project_id)
    targets = Objetivos_especificos.objects.filter(proyecto = project_id)
    project.porcentaje_avance = calacular_porcentaje_avance(project.id)
    project.save()
    return render(request, "admin_project.html", {"project":project, "targets":targets})

def make_project(request):
    if request.method == "POST":
        form=FormProyecto(request.POST,request.FILES)
        if form.is_valid():
            proyecto= form.save(commit=False)
            proyecto.director_id=request.user.id
            proyecto.save()
            return redirect("make_objective",proyecto.id)
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
    form=FormProyecto()           
    return render(request, "make_project.html",{"form": form})

def make_objective(request, project_id):
    if request.method == "POST":
        id_proyecto = Proyecto.objects.get(pk=project_id)
        form=FormObjetivosEspecificos(request.POST,request.FILES)
        if form.is_valid():
            objetivos_especificos= form.save(commit=False)
            objetivos_especificos.proyecto=id_proyecto
            objetivos_especificos.save()       
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
   
    form=FormObjetivosEspecificos() 
    targets = Objetivos_especificos.objects.filter(proyecto = project_id)
    return render(request, "make_objective.html",{"form": form ,'targets':targets,"project_id":project_id})

def delete_objetivo(request,objetive_id):
    try:
        objetivos_especificos = Objetivos_especificos.objects.get(pk=objetive_id)
        
    except Objetivos_especificos.DoesNotExist:
        messages.error(request, "el post a eliminar no existe")


    id_proyecto =objetivos_especificos.proyecto.id
    
    objetivos_especificos.delete()
    print(id_proyecto)
    return redirect("make_objective",id_proyecto)


def delete_student(request, numero_id):
    pass
    try:
        estudiante = Estudiante.objects.get(pk= numero_id)
        
    except Objetivos_especificos.DoesNotExist:
        messages.error(request, "el post a eliminar no existe")

    id_proyecto = estudiante.proyecto.id
    estudiante.delete()
    
    return redirect("manage_students",id_proyecto)

def update_project(request,project_id):
    project = Proyecto.objects.get(id = project_id)
    if request.method == "POST":
        form=FormProyecto(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('admin_project', project_id)
            
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])

    project = Proyecto.objects.get(id =project_id)
    project.porcentaje_avance = calacular_porcentaje_avance(project_id)
    form=FormProyecto(instance=project)
    targets = Objetivos_especificos.objects.filter(proyecto = project_id)
    return render(request, "update_project.html", {"project":project, "targets":targets, "form":form})



def update_student(request, numero_id):
    estudiante = Estudiante.objects.get(pk= numero_id)
    project_id = estudiante.proyecto.id
    if request.method == "POST":
        form = FormStudent(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('manage_students', project_id)
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
    form=FormStudent(instance=estudiante) 
    students = Estudiante.objects.filter(proyecto = project_id)
    return render(request, "manage_students.html", {"form": form,"students":students,'project_id':project_id})

def update_status(request, objetive_id):
    objetive = Objetivos_especificos.objects.get(id = objetive_id)
    objetive.estado = True
    objetive.save()
    project_id =objetive.proyecto.id
    return redirect('admin_project', project_id)

def update_objetive(request, objetive_id):
    objetive = Objetivos_especificos.objects.get(id = objetive_id)
    project_id = objetive.proyecto.id
    if request.method == "POST":
        form=FormObjetivosEspecificos(request.POST, instance=objetive)
        if form.is_valid():
            form.save()
            return redirect('admin_project', project_id)
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
   
    form=FormObjetivosEspecificos(instance=objetive) 
    return render(request, "update_objetive.html",{"form": form, "project_id":project_id})
    

