from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña",  widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'] 
        # help_texts= {k:"" for k in fields}
               
class UserEditForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    email= forms.EmailField(label="Email")
    password1: forms.CharField(label="Contraseña",  widget=forms.PasswordInput, required=False)
    password2: forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    
    class Meta:
        model = User
        fields= ['first_name', 'last_name', 'email', 'password1', 'password2']

class UserEditForm2(forms.Form):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    email= forms.EmailField(label="Email")
    imagen= forms.ImageField(label="Imagen", required=False)

        
# class AvatarForm(forms.Form):
     
#     imagen = forms.ImageField(label="Imagen")
    
#     class Meta:
#         model = Avatar
#         fields = ['imagen']