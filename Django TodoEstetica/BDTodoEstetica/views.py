from django.shortcuts import render
from .models import Producto,Tienda

# Create your views here.

def inicio(request):
    Productos = Producto.objects.all()
    Tiendas = Tienda.objects.all()
    return render(request,'TodoEstetica/index.html', {'Productos':Productos,'Tiendas':Tiendas})

def tienda(request):
    return render(request,'TodoEstetica/tienda.html', {})

def registro(request):
    return render(request,'TodoEstetica/registro.html', {})

def contacto(request):
    return render(request,'TodoEstetica/contacto.html', {})

