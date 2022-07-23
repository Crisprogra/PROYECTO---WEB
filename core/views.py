
from xml.dom.minidom import Entity
import django
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404

from .carrito import Carrito
from .forms import RegistroForm, ContactoForm, CustomUserCreationForm, ProductoForm
from .models import producto
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
def index(request):
    return render(request,'core/index.html')

def home2(request):
    return render(request,'core/home2.html')

def index2(request):
    return render(request,'core/index2.html')

def index3(request):
    return render(request,'core/index3.html')

def index4(request):
    return render(request,'core/index4.html')

def registrar(request):
        data = {
            'form': CustomUserCreationForm()
        }
        if request.method == 'POST':
            formu_registro = CustomUserCreationForm(data=request.POST)
            
            if formu_registro.is_valid:
                formu_registro.save()
                #autenticar al usuario y redirigirlo al home 
                username = formu_registro.cleaned_data['username']
                password = formu_registro.cleaned_data['password1']
                user = authenticate(username=username , password=password)
                login(request, user)
                return redirect (to="index")


        return render(request,'registration/registrar.html',data)
    

def formulario_registro(request):
        datos_registro = {
            'form': RegistroForm()

        }
        if request.method == 'POST':
            formulario_registro = RegistroForm(request.POST)
            
            if formulario_registro.is_valid:
                formulario_registro.save()
                datos_registro['message'] = 'Guardado correctamente'
            else:
                datos_registro['message'] = 'Hubo un problema'
    
        return render(request, 'core/formulario_registro.html',datos_registro)

def index4(request):
        datos_contacto = {
            'form': ContactoForm()

        }
        if request.method == 'POST':
            formulario_contacto = ContactoForm(request.POST)
            
            if formulario_contacto.is_valid:
                formulario_contacto.save()
                datos_contacto['message'] = 'Guardado correctamente'
            else:
                datos_contacto['message'] = 'Hubo un problema'
    
        return render(request, 'core/index4.html',datos_contacto)
        
def index3(request):
    productos = producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos,6)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity' : productos, 
        'paginator': paginator
    }
    return render(request,'core/index3.html',data)   

@permission_required('core.add_producto')
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
            formulario = ProductoForm(request.POST)
            
            if formulario.is_valid:
                formulario.save()
                data['message'] = 'Guardado correctamente'
            else:
                data['message'] = 'Hubo un problema'


    return render(request,'core/agregar.html',data )

@permission_required('core.view_producto')
def listar_producto(request):
    productos = producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos,6)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity' : productos,
        'paginator': paginator
    }

    return render (request, 'core/listar.html', data)

@permission_required('core.change_producto')
def modificar_producto(request,codigoProducto):
    productos = get_object_or_404(producto,codigoProducto=codigoProducto)

    data = {
        'form': ProductoForm(instance=productos)
    }

    if request.method == 'POST':
            formulario = ProductoForm(request.POST, instance=productos)
            
            if formulario.is_valid:
                formulario.save()
                return redirect(to="listar_producto")
            else:
                data['message'] = 'Hubo un problema'


    return render(request, 'core/modificar.html',data )

@permission_required('core.delete_producto')
def eliminar_producto(request,codigoProducto):
    productos = get_object_or_404(producto,codigoProducto=codigoProducto)
    productos.delete()
    return redirect(to="listar_producto")

def agregar_producto_carrito(request,codigoProducto):
    carrito = Carrito(request)
    p = producto.objects.get(codigoProducto=codigoProducto)
    carrito.agregar(p)
    return redirect(to="index3")

def eliminar_producto_carrito(request,codigoProducto):
    carrito = Carrito(request)
    carrito = carrito(request)
    p= producto.objects.get(codigoProducto=codigoProducto)
    carrito.eliminar(p)
    return redirect(to="index3")

def restar_producto_carrito(request,codigoProducto):
    carrito = Carrito(request)
    p = producto.objects.get(codigoProducto=codigoProducto)
    carrito.restar(p)
    return redirect(to="index3")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(to="index3")

