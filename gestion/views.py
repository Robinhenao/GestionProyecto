from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestion.forms import FormStudent
from django.contrib import messages


@login_required(login_url='login')
def gestion(request):
    return render(request, "gestion_proyecto.html")

def manage_students(request):
    return render(request, "manage_students.html")

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

def admin_project(request):
    return render(request, "admin_project.html")

def make_project(request):
    return render(request, "make_projet.html")
