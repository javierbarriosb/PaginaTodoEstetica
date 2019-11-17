from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Producto,Tienda
from django.urls import reverse_lazy


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
   
class ProductoCreate(CreateView):
    model = Producto
    fields = ['NombreProducto','Precio','Descripcion','Marca','Tienda','Imagen']
    success_url = reverse_lazy('inicio:lista')
    
class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['NombreProducto','Precio','Descripcion','Marca','Tienda','Imagen']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('inicio:update',args=[self.object.id])+'?ok'

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('inicio:lista')