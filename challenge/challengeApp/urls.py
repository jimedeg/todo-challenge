
from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    
    path ('accounts/login', login_request, name= "accounts/login"),
    path ('accounts/register', register_request, name= "accounts/register"),
    path ('accounts/logout', logout_request, name= "accounts/logout"),
    path ('accounts/editar_perfil', editar_perfil, name= "accounts/editar_perfil"),

    path ('crear_tarea', crear_tarea, name= "crear_tarea"),   
    path ('tarea_lista/<tarea_id>/', tarea_lista, name= "tarea_lista"), 
    path ('eliminar_tarea/<tarea_id>/', eliminar_tarea, name= "eliminar_tarea"),
    path ('editar_tarea/<tarea_id>/', editar_tarea, name= "editar_tarea"),

]
