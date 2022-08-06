from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# from .forms import *
from .models import *

# Create your views here.

def inicio(request):
    
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