from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('registro/', views.registro, name = 'registro'),
    path('contacto/', views.contacto, name = 'contacto'),


]
