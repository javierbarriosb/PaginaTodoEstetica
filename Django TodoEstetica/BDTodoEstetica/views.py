from django.shortcuts import render


# Create your views here.

def inicio(request):

    return render(request,'TodoEstetica/index.html', {})

def tienda(request):
    return render(request,'TodoEstetica/tienda.html', {})

def registro(request):
    return render(request,'TodoEstetica/registro.html', {})

def contacto(request):
    return render(request,'TodoEstetica/contacto.html', {})

