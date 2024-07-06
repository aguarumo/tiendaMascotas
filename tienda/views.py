from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto


# Create your views here.



def index(request):
    context={}
    return render(request, 'tienda/index.html', context)

def tienda_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': list(productos.values())
    }
    return JsonResponse(data)

def tienda(request):
    return render(request, 'tienda/tienda.html')

def nosotros(request):
    return render(request, 'tienda/nosotros.html')