from django.db import models

# Create your models here.

class registro(models.Model):
    nombreUsuario = models.CharField(primary_key=True,max_length=50,verbose_name='Nombre del usuario')
    correoUsuario = models.CharField(max_length=100,verbose_name='Correo del usuario')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellidoPaterno = models.CharField(max_length=50,verbose_name='Apellido paterno')
    apellidoMaterno = models.CharField(max_length=50,verbose_name='Apellido materno')
    direccion = models.CharField(max_length=100,verbose_name='Direccion')
    passwordUsuario = models.CharField(max_length=200,verbose_name='Contraseña del usuario')

    def __str__(self) :
        return  self.nombreUsuario


class producto(models.Model):
    codigoProducto = models.CharField(primary_key=True,max_length=5,verbose_name='Codigo del producto')
    imagenProducto = models.CharField(max_length=200,verbose_name='Imagen del producto')
    nombreProducto = models.CharField(max_length=200,verbose_name='Nombre del producto')
    descripcionProducto = models.CharField(max_length=500,verbose_name='Descripcion del producto')  
    precioProducto = models.IntegerField(verbose_name='Precio del producto')    

    def __str__(self) :
        return  self.nombreProducto
  


class contacto(models.Model):
    nombreContacto = models.CharField(max_length=200,verbose_name='Nombre del contacto')
    correoContacto = models.CharField(max_length=200,verbose_name='Correo del contacto')
    comentarioContacto = models.TextField(max_length=1000,verbose_name='Comentario del contacto ')

    def __str__(self) :
        return  self.nombreContacto
    
