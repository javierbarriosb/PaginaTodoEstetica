from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'TodoEstetica/post_list.html', {})

def tienda(request):
    return render(request,'TodoEstetica/tienda.html', {})

