from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Producto,Tienda

# Create your views here.


class inicio(TemplateView):
     template_name = "BDTodoEstetica/index.html"
     def get (self,request, *args, **kwargs):
        Productos = Producto.objects.all()
        Tiendas = Tienda.objects.all()
        return render (request, self.template_name,{'Productos':Productos,'Tiendas':Tiendas})

class registro (TemplateView):
     template_name = "BDTodoEstetica/registro.html"

class contacto (TemplateView):
    template_name = "BDTodoEstetica/contacto.html"

class listProducto(ListView):
    model = Producto

class DetailProducto(DetailView):
    model = Producto


