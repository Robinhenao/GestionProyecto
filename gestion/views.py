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


def manage_students(request):
    students = Estudiante.objects.filter(proyecto = 1)
    return render(request, "manage_students.html",{"students":students})

def make_student(request):
    if request.method == "POST":
        form=FormStudent(request.POST,request.FILES)
        if form.is_valid():
            estudiante= form.save(commit=False)
            estudiante.save()
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
    form=FormStudent()           
    return render(request, "make_student.html",{"form": form})


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
        idid = Proyecto.objects.get(pk=project_id)
        form=FormObjetivosEspecificos(request.POST,request.FILES)
        if form.is_valid():
            objetivos_especificos= form.save(commit=False)
            objetivos_especificos.proyecto=idid
            objetivos_especificos.save()
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
    form=FormObjetivosEspecificos() 
    targets = Objetivos_especificos.objects.filter(proyecto = project_id)          
    return render(request, "make_objective.html",{"form": form, 'targets':targets})
