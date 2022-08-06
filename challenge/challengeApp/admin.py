from django.contrib import admin

from .models import *

# Register your models here.

class AvatarAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'imagen')
    
    
    
    
    

admin.site.register(Avatar, AvatarAdmin)