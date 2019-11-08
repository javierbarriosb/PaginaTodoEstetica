from django.urls import path
from . import views
from .views import registro,inicio,contacto,listProducto,DetailProducto

urlpatterns = [
    path('', inicio.as_view(), name = 'inicio'),
    path('registro/',registro.as_view(), name = 'registro'),
    path('contacto/', contacto.as_view(),name = 'contacto'),
    path('lista/',listProducto.as_view(),name ='lista'), 
    path('<int:pk>/',DetailProducto.as_view(),name ='detail'), 
] 
