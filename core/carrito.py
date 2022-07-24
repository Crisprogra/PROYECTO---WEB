from ast import Delete
from math import prod
from operator import truediv

from .models import producto


class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito") 
        if not carrito:
            self.session["carrito"]= {}
            self.carrito =self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, p):
        
        codigoProducto = str(p.codigoProducto)
        if codigoProducto not in self.carrito.keys():
            self.carrito[codigoProducto]={
                "codigoProducto": p.codigoProducto,
                "Nombre": p.nombreProducto,
                "Total": p.precioProducto,
                "Precio": p.precioProducto,
                "Cantidad": 1,
            }
        else:
            self.carrito[codigoProducto]["Cantidad"] += 1
            self.carrito[codigoProducto]["Total"] += p.precioProducto
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self,p):
        codigoProducto = str(p.codigoProducto)
        if codigoProducto in self.carrito:
            del self.carrito[codigoProducto]
            self.guardar_carrito()
    
    def restar(self,p):
        codigoProducto = str(p.codigoProducto)
        if codigoProducto  in self.carrito.keys():
            self.carrito[codigoProducto]["Cantidad"] -=1
            self.carrito[codigoProducto]["Total"] -= p.precioProducto
            if self.carrito[codigoProducto]["Cantidad"]<=0: self.eliminar[p]
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] ={}
        self.session.modified = True
        


