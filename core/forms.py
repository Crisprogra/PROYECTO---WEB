from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import contacto, registro

#creando una clase para el formulario desde la base de datos
class RegistroForm(ModelForm):

    class Meta:
        model = registro
        fields = ['nombreUsuario','correoUsuario','nombre','apellidoPaterno','apellidoMaterno','direccion','passwordUsuario']


class ContactoForm(ModelForm):

    class Meta:
        model = contacto
        fields = ['nombreContacto','correoContacto','comentarioContacto']
