
from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    
    path ('accounts/login', login_request, name= "accounts/login"),
    path ('accounts/register', register_request, name= "accounts/register"),
    # path ('accounts/logout', logout_request, name= "accounts/logout"),
    # path ('accounts/editar_perfil', editar_perfil, name= "accounts/editar_perfil"),
    
    
]
