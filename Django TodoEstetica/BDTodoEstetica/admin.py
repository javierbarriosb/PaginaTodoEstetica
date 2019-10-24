from django.contrib import admin
from .models import Producto,Cliente,Tienda,Vendedore

# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Tienda)
admin.site.register(Vendedore)
