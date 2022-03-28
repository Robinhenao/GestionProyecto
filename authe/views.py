from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages

def login_session(request):
    if request.method== "POST":
        form =AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre,password=password)
            if usuario is  not None:
                login(request,usuario)
                messages.success(request,F"Welcome {nombre}" )
                return redirect("")
            else:
                messages.error(request,"Datos incorrectos")
        else:
            messages.error(request, "Datos incorrectos")

    form= AuthenticationForm()
    return render(request,"login.html",{"form":form})

def logout_session(request):
    logout(request)
    messages.success(request,F"Logout ")
    return redirect("login")


class view_Registro(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,"registro.html",{"form":form})

    def post(self, request):
        form =UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            nombre=form.cleaned_data.get("username")
            messages.success(request,f"registro exitoso {nombre}")
            login(request,usuario)
            return redirect("foro")
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,"registro.html",{"form":form})