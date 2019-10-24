from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'TodoEstetica/index.html', {})

def tienda(request):
    return render(request,'TodoEstetica/tienda.html', {})

