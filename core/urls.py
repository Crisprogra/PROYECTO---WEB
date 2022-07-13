from django import urls
from django.urls import path
from .views import agregar_producto_carrito, eliminar_producto_carrito, index, index2, index3, index4, formulario_registro, registrar,agregar_producto,listar_producto, modificar_producto,eliminar_producto, restar_producto_carrito,limpiar_carrito


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
    path('agregar/<int:producto_id>/', agregar_producto_carrito, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto_carrito, name="Del"),
    path('restar/<int:producto_id>/', restar_producto_carrito, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),

   



]