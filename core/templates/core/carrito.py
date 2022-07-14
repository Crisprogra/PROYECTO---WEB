from ast import Delete
from math import prod
from operator import truediv


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

    def agregar(self,p):
        codigo = str(p.codigoProducto)
        if codigo not in self.carrito.keys():
            self.carrito[codigo]= {
                "Codigo_producto": p.codigoProducto,
                "Nombre": p.nombreProducto,
                "Total": p.precioProducto,
                "Cantidad": 1
            }
        else:
            self.carrito[codigo]["Cantidad"]+=1
            self.carrito[codigo]["Total"]= p.precioProducto
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self,p):
        codigo = str(p.codigoProducto)
        if codigo in self.carrito:
            del self.carrito[codigo]
            self.guardar_carrito()
    def restar(self,p):
        codigo = str(p.codigoProducto)
        if codigo  in self.carrito.keys():
            self.carrito[codigo]["Cantidad"] -=1
            self.carrito[codigo]["Total"] -= p.precioProducto
            if self.carrito[codigo]["Cantidad"]<=0: self.eliminar[p]
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] ={}
        self.session.modified = True
        


