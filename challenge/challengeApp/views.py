from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *

from django.contrib import messages

# Create your views here.

def inicio(request):
    
    if request.user.is_authenticated:
        
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatar/generica.jpg"
            return render(request, "challengeApp/index.html", {"url": url})
    
    return render(request, 'challengeApp/index.html')

def login_request(request):
    
    if request.method == 'POST':
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return render(request, 'challengeApp/login.html', {'form': form})
        else:
            return render(request, 'challengeApp/login.html', {'form': form})
    
    form = AuthenticationForm()
    
    return render(request, 'challengeApp/login.html', {'form': form} )

def register_request(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            form.save()
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        
        password1 = form.data['password1']
        password2 = form.data['password1']
        
        for msg in form.errors.as_data():
            if msg == 'email':
                messages.error(request, "El correo es invalido o ya existe.")
            if msg == 'username':
                messages.error(request, "El nombre de usuario es invalido o ya existe.")
            if msg == 'password2' and password1 == password2:
                messages.error(request, "La contraseña elegida no cumple los requisitos.")
            elif msg == 'password2' and password1 != password2:
                messages.error(request, "Las contraseñas no coinciden.")
            
        return render(request, 'challengeApp/register.html', {'form': form})
    
    form = UserRegisterForm()
    
    return render(request, 'challengeApp/register.html', {'form': form} )

def logout_request(request):
    
    logout(request)
    return redirect("inicio")


