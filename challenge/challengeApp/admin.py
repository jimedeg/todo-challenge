from django.contrib import admin

from .models import *

# Register your models here.

class AvatarAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'imagen')
    
class TareaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'fecha', 'completada') 
    
    
    

admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Tarea, TareaAdmin)