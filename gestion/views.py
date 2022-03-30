from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def gestion(request):
    return render(request, "gestion_proyecto.html")

def manage_students(request):
    return render(request, "manage_students.html")

def make_student(request):
    return render(request, "make_student.html")

def admin_project(request):
    return render(request, "admin_project.html")

def make_project(request):
    return render(request, "make_projet.html")

