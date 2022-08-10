from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatar/', blank=True)

class Tarea(models.Model):
    
    texto = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.texto
    
    class Meta:
        ordering = ['completada']
    
    