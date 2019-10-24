from django.db import models

# Create your models here.
class Cliente (models.Model):   

    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=60)
    Correo = models.EmailField(primary_key=True,max_length=50) #primary
    Contraseña = models.CharField(max_length=20)
    

class Tienda (models.Model):
    
    NombreTienda = models.CharField(max_length=40)
    Rut_Tienda = models.EmailField(primary_key=True,max_length=15)
    
class Vendedore (models.Model):

    RutVendedor = models.CharField(max_length=12)
    NombreVendedor =models.CharField(primary_key=True,max_length=20)
    Tienda = models.ForeignKey('Tienda',on_delete=models.CASCADE)
    CorreoVendedor = models.EmailField(max_length=50)
    Mensaje = models.TextField()

class Producto (models.Model):
    
    NombreProducto = models.CharField(max_length=20)  
    Precio = models.CharField(max_length=8)
    Descripcion = models.TextField()
    Marca = models.CharField(max_length=20)
    Imagen = models.ImageField(upload_to="ImagenProductos")

    def __str__(self):
        return self.NombreProducto
    