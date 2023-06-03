from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from ProyectoApp.Carrito import Carrito
from ProyectoApp.models import Platillos
from ProyectoApp.models import Tickets

def index(request):
    idti = Tickets.objects.all().last()
    datosMesa = MesaInfo.objects.all().last()
    entradas = Platillos.objects.filter(categoria = 1)
    principales = Platillos.objects.filter(categoria = 2)
    bebidas = Platillos.objects.filter(categoria = 3)
    postres = Platillos.objects.filter(categoria = 4)
    helados = Platillos.objects.filter(categoria = 5)
    return render(request,'index.html', {'entradas':entradas, 'principales':principales, 'bebidas':bebidas, 'postres':postres, 'helados':helados, 'idti':idti, 'datosMesa':datosMesa})

def inicioMesa(request):
    idMes = MesaInfo.objects.all().last()
    return render(request,'inicioMesa.html', {'idMes':idMes})

def registroMesa(request):
    idMes = request.POST['idMes']
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    mesa = MesaInfo.objects.create(id=idMes,Mesa=txt1,NoMesa=txt2,Contraseña=txt3,Ubicacion=txt4)
    mesa.save()
    return redirect("ProyectoApp:index")

def votacion(request):
    helados = Platillos.objects.filter(categoria = 5)
    return render(request,'votacion.html',{'helados':helados})

def inicio(request):
    return render(request,'inicio.html')

def loginResponsable(request):
    return render(request,'loginResponsable.html')

def compruebaLog(request):
    uR = request.POST['userR1']
    pR = request.POST['passR1']
    if Responsables.objects.filter(usuarioR = uR).exists() and not Responsables.objects.filter(contraseñaR = pR).exists():
        messages.success(request, 'Tu contraseña no es correcta')
        return render(request,'loginResponsable.html')
    elif not Responsables.objects.filter(usuarioR = uR).exists() and Responsables.objects.filter(contraseñaR = pR).exists():
        messages.success(request, 'Tu usuario no es correcto')
        return render(request,'loginResponsable.html')
    elif not Responsables.objects.filter(usuarioR = uR).exists() and not Responsables.objects.filter(contraseñaR = pR).exists():
        messages.success(request, 'Ninguno de los campos es correcto')
        return render(request,'loginResponsable.html')
    else:
        admin = authenticate(username="123", password="123")
        login(request,admin)
        return redirect("ProyectoApp:inicioMesa")

def agregar_Platillo(request, platillos_id):
    carrito = Carrito(request)
    platillos = Platillos.objects.get(id=platillos_id)
    carrito.agregar(platillos)
    return redirect("ProyectoApp:index")

def eliminar_Platillo(request, platillos_id):
    carrito = Carrito(request)
    platillos = Platillos.objects.get(id=platillos_id)
    carrito.eliminar(platillos)
    return redirect("ProyectoApp:index")

def restar_Platillo(request, platillos_id):
    carrito = Carrito(request)
    platillos = Platillos.objects.get(id=platillos_id)
    carrito.restar(platillos)
    return redirect("ProyectoApp:index")

def limpiar_Platillo(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("ProyectoApp:index")

def agregar_ticket(request):
    arreglo = request.POST['arreglo']
    print(len(arreglo))
    arreglo = arreglo.split(",")
    print(arreglo)
    s = int(len(arreglo)/3)
    print(len(arreglo))
    arreglo = splita(arreglo, s)
    print(arreglo)
    cont = 0
    for x in range(s):
        id_ticket = request.POST['id_ticket']
        nombre = arreglo[cont][0]
        precio = arreglo[cont][1]
        cantidad = arreglo[cont][2]
        cont+=1
        ticket=Tickets.objects.create(id_ticket=id_ticket,nombre=nombre,precio=precio,cantidad=cantidad)
        ticket.save()
    return redirect("ProyectoApp:votacion")

def splita(arr, size):
    arrs = []
    cont = 0
    eli = 0
    for x in range(size):
        arrs.append([])
    for x in range(len(arr)):
        if cont == 3:
           cont = 0
           eli +=1
        arrs[eli].append(arr[x])
        cont+=1
    return arrs
