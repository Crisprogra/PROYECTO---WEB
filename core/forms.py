from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import contacto, registro, producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#creando una clase para el formulario desde la base de datos
class RegistroForm(ModelForm):

    class Meta:
        model = registro
        fields = ['username','email','first_name','last_name','direccion','password']


class ContactoForm(ModelForm):

    class Meta:
        model = contacto
        fields = ['nombreContacto','correoContacto','comentarioContacto']


class ProductoForm(ModelForm):

    class Meta:
        model = producto
        fields = ['codigoProducto', 'imagenProducto', 'nombreProducto','descripcionProducto', 'precioProducto']




class CustomUserCreationForm(UserCreationForm):

    
    pass


