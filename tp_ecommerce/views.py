from django.urls import path
from . import views
from django.shortcuts import render

def index(request):
    return render(request, 'app_ecommerce/index.html')

def cliente(request):
    return render(request, 'app_ecommerce/cliente_form.html')

def producto(request):
    return render(request, 'app_ecommerce/producto_form.html')

def pedido(request):
    return render(request, 'app_ecommerce/pedido_form.html')

def buscar(request):
    return render(request, 'app_ecommerce/buscar.html')
