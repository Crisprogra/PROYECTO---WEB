from django import urls
from django.urls import path
from .views import index, index2, index3, index4, formulario_registro, registrar,agregar_producto,listar_producto, modificar_producto,eliminar_producto


urlpatterns =[
    path('',index,name="index"),
    path('Sobre Nosotros',index2,name="index2"),
    path('Tienda',index3,name="index3"),
    path('Contacto',index4,name="index4"),
    path('Registro',formulario_registro,name="formulario_registro"),
    path('Registrar',registrar,name="registrar"),
    path('agregar-producto',agregar_producto,name="agregar_producto"),
    path('listar-producto',listar_producto,name="listar_producto"),
    path('modificar-producto/<codigoProducto>',modificar_producto,name="modificar_producto"),
    path('eliminar-producto/<codigoProducto>',eliminar_producto,name="eliminar_producto"),

   



]