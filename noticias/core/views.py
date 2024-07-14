from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden, HttpResponse
from .serializers import *
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


#from django.core.pagintator import


# Create your views here.



def index (request):
    return render(request, 'core/index.html')

def login (request):
    return render(request, 'core/login.html')


def category (request):
    return render(request, 'core/category.html')

def contact (request):
    return render(request, 'core/contact.html')

def base (request):
    return render(request, 'core/base.html')


class TipoEmpleadoViewset(viewsets.ModelViewSet):
    queryset = TipoEmpleado.objects.all()
    serializer_class = TipoEmpleadoSerializer
    renderer_classes = [JSONRenderer]


class GeneroViewset(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    renderer_classes = [JSONRenderer]

class EmpleadoViewset(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    renderer_classes = [JSONRenderer]


def register(request):
    aux = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            
            group = Group.objects.get(name='cliente')
            user.groups.add(group)
            
            
            return redirect(to="empleados")
        else:
            aux['form'] = formulario
            

    return render(request, 'registration/register.html', aux)


def account_locked (request):
      return render(request, 'core/account_locked.html')  



@login_required
def empleados (request):
    empleados = Empleado.objects.all()
    aux = {
        'lista' : empleados
    }

    return render(request, 'core/index.html', aux)


@login_required
def empleadosadd(request):
    aux = {
        'form': EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Empleado Agregado Correctamente'
        else:
            aux['form'] = formulario
            aux['msj'] = 'Error al agregar Empleado'

    return render(request, 'core/empleados/crud/add.html', aux)


@login_required
def empleadosupdate (request, id):
    empleado = Empleado.objects.get(id=id)
    aux = {
        'form': EmpleadoForm(instance=empleado)
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleado,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            aux['msj'] = 'Empleado Modificado Correctamente'
        else:
            aux['form'] = formulario
            aux['msj'] = 'Error al modificar Empleado'
    return render(request, 'core/empleados/crud/update.html', aux)


@login_required
def empleadosdelete (request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect (to="empleados")


def noticia_1 (request):
    return render(request, 'core/noticias/noticia 1.html')

def noticia_2 (request):
    return render(request, 'core/noticias/noticia 2.html')

def noticia_3 (request):
    return render(request, 'core/noticias/noticia 3.html')

def noticia_4 (request):
    return render(request, 'core/noticias/noticia 4.html')

def noticia_5 (request):
    return render(request, 'core/noticias/noticia 5.html')

def noticia_6 (request):
    return render(request, 'core/noticias/noticia 6.html')

def noticia_7 (request):
    return render(request, 'core/noticias/noticia 7.html')

def noticia_8 (request):
    return render(request, 'core/noticias/noticia 8.html')

def noticia_9 (request):
    return render(request, 'core/noticias/noticia 9.html')

def noticia_10 (request):
    return render(request, 'core/noticias/noticia 10.html')

def noticia_11 (request):
    return render(request, 'core/noticias/noticia 11.html')

def noticia_12 (request):
    return render(request, 'core/noticias/noticia 12.html')

def noticia_13 (request):
    return render(request, 'core/noticias/noticia 13.html')

def noticia_14 (request):
    return render(request, 'core/noticias/noticia 14.html')

def noticia_15 (request):
    return render(request, 'core/noticias/noticia 15.html')

def noticia_16(request):
    return render(request, 'core/noticias/noticia 16.html')

def noticia_17 (request):
    return render(request, 'core/noticias/noticia 17.html')

def noticia_18 (request):
    return render(request, 'core/noticias/noticia 18.html')

def noticia_19 (request):
    return render(request, 'core/noticias/noticia 19.html')

def noticia_20 (request):
    return render(request, 'core/noticias/noticia 20.html')

def noticia_21 (request):
    return render(request, 'core/noticias/noticia 21.html')

def noticia_22 (request):
    return render(request, 'core/noticias/noticia 22.html')

def noticia_23 (request):
    return render(request, 'core/noticias/noticia 23.html')

def noticia_24 (request):
    return render(request, 'core/noticias/noticia 24.html')

def noticia_25 (request):
    return render(request, 'core/noticias/noticia 25.html')

def noticia_26 (request):
    return render(request, 'core/noticias/noticia 26.html')

def noticia_27 (request):
    return render(request, 'core/noticias/noticia 27.html')

def noticia_28 (request):
    return render(request, 'core/noticias/noticia 28.html')

def noticia_29 (request):
    return render(request, 'core/noticias/noticia 29.html') 

def clima (request):
    return render(request, 'core/noticias/clima.html')

def EE_UU (request):
    return render(request, 'core/noticias/EE.UU.html')

def Mexico (request):
    return render(request, 'core/noticias/Mexico.html')

def Salud (request):
    return render(request, 'core/noticias/Salud.html')

def Mundo (request):
    return render(request, 'core/noticias/Mundo.html')

def Deportes (request):
    return render(request, 'core/noticias/Deportes.html')

def Mundo (request):
    return render(request, 'core/noticias/Mundo.html')

def suscripcíon (request):
    return render(request, 'core/suscripcíon.html')

def carrito (request):
    return render(request, 'core/carrito.html')

def generate_voucher_pdf(request, subscription_type):
    # Crear el PDF del voucher
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="voucher.pdf"'

    # Crear el contenido del PDF con los detalles de la suscripción
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, f"Voucher de Suscripción - {subscription_type}")
    p.drawString(100, 730, "Detalles adicionales...")
    # Aquí puedes agregar más detalles según necesites

    p.showPage()
    p.save()

    return response