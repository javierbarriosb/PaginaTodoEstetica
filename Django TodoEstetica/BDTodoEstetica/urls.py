from django.urls import path
from django.conf import settings
from . import views
from django.contrib.auth.decorators import login_required 
from .views import registro,inicio,contacto,listProducto,DetailProducto,ProductoCreate,ProductoUpdate,ProductoDelete

pages_patterns = ([
    path('', inicio.as_view(), name = 'inicio'),
    path('registro/',registro.as_view(), name = 'registro'),
    path('contacto/', contacto.as_view(),name = 'contacto'),
    path('lista/',listProducto.as_view(),name ='lista'), 
    path('<int:pk>/',DetailProducto.as_view(),name ='detail'), 
    path('create/',ProductoCreate.as_view(),name='create'),
    path('update/<int:pk>/',ProductoUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',ProductoDelete.as_view(),name='delete'),
],'inicio')
