from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import Producto
from django.contrib import messages
from .forms import ProductoForm
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

def admin_index(request):
    context={}
    return render(request, 'tienda/admin_index.html', context)

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

def creacion_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
        else:
            messages.error(request, 'Error al añadir el producto.')
    else:
        form = ProductoForm()
    return render(request, 'tienda/creacion_producto.html', {'form': form})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('lista_productos')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo {field}: {error}")
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/formulario_producto.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado con éxito.')
        return redirect('lista_productos')
    return render(request, 'tienda/confirmacion_eliminar_producto.html', {'producto': producto})