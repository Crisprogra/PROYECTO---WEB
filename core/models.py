
from django.db import models

# Create your models here.

class registro(models.Model):
    username = models.CharField(primary_key=True,max_length=50,verbose_name='Nombre del usuario')
    email = models.CharField(max_length=100,verbose_name='Correo del usuario')
    first_name = models.CharField(max_length=50,verbose_name='Nombre')
    last_name = models.CharField(max_length=50,verbose_name='Apellidos')
    direccion = models.CharField(max_length=100,verbose_name='Direccion')
    password = models.CharField(max_length=200,verbose_name='Contraseña del usuario')

    def __str__(self) :
        return  self.username


class producto(models.Model):
    codigoProducto = models.CharField(primary_key=True,max_length=5,verbose_name='Codigo del producto')
    imagenProducto = models.CharField(max_length=200,verbose_name='Imagen del producto')
    nombreProducto = models.CharField(max_length=200,verbose_name='Nombre del producto')
    descripcionProducto = models.CharField(max_length=500,verbose_name='Descripcion del producto')  
    precioProducto = models.IntegerField(verbose_name='Precio del producto')    

    def __str__(self) :
        return  f'{self.nombreProducto} -> {self.precioProducto}'
  


class contacto(models.Model):
    nombreContacto = models.CharField(max_length=200,verbose_name='Nombre del contacto')
    correoContacto = models.CharField(max_length=200,verbose_name='Correo del contacto')
    comentarioContacto = models.TextField(max_length=1000,verbose_name='Comentario del contacto ')

    def __str__(self) :
        return  self.nombreContacto
    

