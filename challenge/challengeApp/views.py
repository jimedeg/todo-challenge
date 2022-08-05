from django.shortcuts import render

from .views import *

# Create your views here.

def inicio(request):
    
    return render(request, 'challengeApp/index.html')