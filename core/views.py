
from django.shortcuts import redirect, render
from .forms import RegistroForm, ContactoForm, CustomUserCreationForm
from .models import producto
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'core/index.html')

def index2(request):
    return render(request,'core/index2.html')

def index3(request):
    return render(request,'core/index3.html')

def index4(request):
    return render(request,'core/index4.html')

def registrar(request):
        datos_registro = {
            'form': CustomUserCreationForm()
        }
        if request.method == 'POST':
            formulario_registro = CustomUserCreationForm(datos_registro=request.POST)
            
            if formulario_registro.is_valid:
                formulario_registro.save()
                #autenticar al usuario y redirigirlo al home 
                username = formulario_registro.cleaned_data['username']
                password = formulario_registro.cleaned_data['password1']
                user = authenticate(username=username , password=password)
                login(request, user)
                return redirect (to="index")


        return render(request,'registration/registrar.html',datos_registro)
    

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