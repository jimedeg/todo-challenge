from django.shortcuts import render, redirect
from django.db.models import Q


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

from django.contrib import messages

# Create your views here.

@login_required
def inicio(request):
    tareas = Tarea.objects.all()
    
    form = TareaForm()
              
    
    if request.method == "POST":
        
        buscar = request.POST["buscar"]
        
        if buscar != "":
            tareas = Tarea.objects.filter(Q(texto__icontains=buscar) | Q(fecha__icontains=buscar)).values()
            
            return render(request, "challengeApp/index.html", { "tareas": tareas, "buscar": True, "busqueda":buscar})
    
    if request.user.is_authenticated:
        
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatar/generica.jpg"
            return render(request, "challengeApp/index.html", {"url": url})
    
    return render(request, 'challengeApp/index.html', {"tareas": tareas, "buscar": False, "form": form})

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

@login_required
def editar_perfil(request):
    
    user = request.user    
    try:
        avatar = Avatar.objects.get(usuario=user)
    except:
        avatar = Avatar(usuario=user)
        avatar.save()
    
    if request.method == "POST":
        
        form = UserEditForm2(request.POST, request.FILES)
        
        if form.is_valid():
            
            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]

            user.save()
            messages.success(request, "Perfil actualizado con éxito!")

            if info['imagen'] != None:
                avatar.imagen = info['imagen']
                avatar.save()
                           
            return redirect("inicio")
                
        else:
            messages.error(request, "Error al actualizar el perfil")
            return render(request, "challengeApp/editar_perfil.html", {"form": form})          
    
    else:
         form = UserEditForm2(initial={"email": user.email,
                                      "first_name": user.first_name, 
                                      "last_name": user.last_name, 
                                      "imagen": avatar.imagen
                                      })
    
    return render(request, "challengeApp/editar_perfil.html", {"form": form})

@login_required
def crear_tarea(request):
    
    if request.method == "POST":
        
        form = TareaForm(request.POST)
        
        if form.is_valid():
            
            form_tarea = form.cleaned_data
            tareas = Tarea(texto=form_tarea["texto"])
            tareas.save()
            messages.success(request, "Tarea creada con éxito!")
            return redirect("inicio")
    
    else:
        form = TareaForm()
    
    return render(request, "challengeApp/index.html", {"form": form})

@login_required
def eliminar_tarea(request, tarea_id):
    
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    
    return redirect("inicio")

@login_required
def tarea_lista(request, tarea_id):
    
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.completada = True
    tarea.save()
    return redirect("inicio")

def desmarcar_tarea(request, tarea_id):
    
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.completada = False
    tarea.save()
    return redirect("inicio")

@login_required
def editar_tarea(request, tarea_id):
    
    tarea = Tarea.objects.get(id=tarea_id)
    
    if request.method == "POST":
        
        form = TareaForm(request.POST)
        
        if form.is_valid():
            
            form_tarea = form.cleaned_data
            
            tarea.texto = form_tarea["texto"]
            tarea.save()
            messages.success(request, "Tarea actualizada con éxito!")
            return redirect("inicio")
    
    else:
        form = TareaForm(initial={"texto": tarea.texto})
    
    return render(request, "challengeApp/editar_tarea.html", {"form": form})