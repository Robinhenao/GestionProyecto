from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from gestion.forms import FormStudent
from gestion.forms import FormProyecto
from gestion.forms import FormObjetivosEspecificos
from gestion.forms import FormProyecto, FormStudent
from gestion.models import Estudiante, Objetivos_especificos, Proyecto
from django.core.paginator import Paginator
from django.contrib import messages


@login_required(login_url='login')


def gestion(request):
    listado_posts =Proyecto.objects.all()
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
    return render(request, "admin_project.html", {"project":project, "targets":targets})

def make_project(request):
    if request.method == "POST":
        form=FormProyecto(request.POST,request.FILES)
        if form.is_valid():
            proyecto= form.save(commit=False)
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
    return render(request, "make_objective.html",{"form": form ,'targets':targets})

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



