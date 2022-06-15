
from django.shortcuts import render
from .forms import RegistroForm, ContactoForm, CustomUserForm
from .models import producto
# Create your views here.
def index(request):
    return render(request,'core/index.html')

def index2(request):
    return render(request,'core/index2.html')

def index3(request):
    return render(request,'core/index3.html')

def index4(request):
    return render(request,'core/index4.html')

def registro(request):
        datos_registro = {
            'form': CustomUserForm()
        }
        return render(request,'core/registration/registrar.html',datos_registro)
    

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
    datos = {
        'productos' : productos
    }
    return render(request,'core/index3.html',datos)       