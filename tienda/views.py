from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_admin:
                return redirect('tienda/admin_index')  
        else:
            messages.error(request, 'Credenciales inválidas.')
    return render(request, 'tienda/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')