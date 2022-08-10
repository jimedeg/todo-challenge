from django.test import TestCase

from .models import *
from .forms import *
from .views import *

# Create your tests here.
class TareaTest(TestCase):
    
    def setUp(self):
        Tarea.objects.create(texto="ver pelis 2",completada= False)
        
    def test_tarea_texto(self):
        tarea = Tarea.objects.get(completada = False)
        self.assertEqual(tarea.texto, "ver pelis 2")
    
    def test_tarea_creado(self):
        tarea = Tarea.objects.get(completada = False)
        self.assertNotEquals(tarea, None)

class editar_tarea(TestCase):
    
    def setUp(self):
        self.data = {
            "texto": "ver pelis 2",
            "completada": False }
        
    def test_editar_tarea(self):
        form = TareaForm(self.data)
        self.assertTrue(form.is_valid())  
   

class test_registro_usuario(TestCase):
    
    def setUp(self):
        self.data = {
            "username": "jime_deg",
            "password1": "jimena_8",
            "password2": "jimena_8",
            "email": "jimena@gmail.com" }
        
    def test_registro_usuario(self):
        form = UserCreationForm(self.data)
        self.assertTrue(form.is_valid())
        
class test_login_usuario(TestCase):
    
    def setUp(self):
        self.data = {
            "username": "jime_deg",
            "password": "jimena_8" }
        
    def test_login_usuario(self):
        form = AuthenticationForm(None, self.data)
        self.assertFalse(form.is_valid())

class editar_perfil(TestCase):
    
    def setUp(self):
        self.data = {
            "username": "jime_deg",
            "password": "jimena_8",
            "email": "jimena@deg.com" }
    
    def test_editar_perfil(self):
        form = UserEditForm2(self.data)
        self.assertFalse(form.is_valid())

              