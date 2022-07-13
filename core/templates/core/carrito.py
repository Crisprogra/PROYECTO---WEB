from ast import Delete
from math import prod
from operator import truediv


class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"]= {}
            self.carrito =self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self,producto):
        codigo = str(producto.codigoProducto)
        if codigo not in self.carrito.keys():
            self.carrito[codigo]= {
                "Codigo": producto.codigoProducto,
                "Nombre": producto.nombreProducto,
                "Total": producto.precioProducto,
                "Cantidad": 1
            }
        else:
            self.carrito[codigo]["Cantidad"]+=1
            self.carrito[codigo]["Total"]= producto.precioProducto
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self,producto):
        codigo = str(producto.codigoProducto)
        if codigo in self.carrito:
            del self.carrito[codigo]
            self.guardar_carrito()
    def restar(self,producto):
        codigo = str(producto.codigoProducto)
        if codigo  in self.carrito.keys():
            self.carrito[codigo]["Cantidad"] -=1
            self.carrito[codigo]["Total"] -= producto.precioProducto
            if self.carrito[codigo]["Cantidad"]<=0: self.eliminar[producto]
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] ={}
        self.session.modified = True
        


