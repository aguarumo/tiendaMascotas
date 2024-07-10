from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from .models import Producto,Usuario,Profile
from django.contrib import messages
from .forms import ProductoForm,RegistroForm,ActualizacionUsuarioForm,UserProfileForm,LoginForm
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

def contacto(request):
    return render(request, 'tienda/contacto.html')

def donaciones(request):
    return render(request, 'tienda/donaciones.html')

def formulario(request):
    return render(request, 'tienda/formulario.html')

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
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('lista_productos')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = ProductoForm()
    
    context = {
        'form': form
    }
    return render(request, 'tienda/creacion_producto.html', context)

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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('admin_index')  # Redirigir a la página principal o donde desees
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'tienda/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        
            return redirect(request.session.get('previous_page', 'manage_users'))
        else:
            return render(request, 'processes/register.html', {'form': form, 'errors': form.errors})
    else:
        request.session['previous_page'] = request.META.get('HTTP_REFERER', 'manage_users')
        form = RegistroForm()
    return render(request, 'processes/register.html', {'form': form})

def manage_usuarios(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'tienda/manage_usuarios.html', context)

def user_list(request):
    users = Usuario.objects.all()
    context = {'users': users}
    return render(request, 'tienda/manage_usuarios.html', context)

def find_edit_user(request, user_id):
    user = get_object_or_404(Usuario, id=user_id)
    context = {'user': user}
    return render(request, 'tienda/update_user.html', context)

def update_user(request, user_id):
    user = get_object_or_404(Usuario, id=user_id)

    if request.method == "POST":
        form = ActualizacionUsuarioForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect('manage_usuarios')
        else:
            messages.error(request, "Por favor corrige los errores a continuación.")
            context = {'form': form, 'user': user}
            return render(request, 'tienda/update_user.html', context)
    else:
        form = ActualizacionUsuarioForm(instance=user)
        context = {'form': form, 'user': user}
        return render(request, 'tienda/update_user.html', context)

def delete_user_view(request, user_id):
    user = get_object_or_404(Usuario, id=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "Usuario eliminado exitosamente.")
        return redirect('manage_usuarios')
    return render(request, 'tienda/confirm_delete.html', {'user': user})

def profile_view(request):
    user = request.user  
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = UserProfileForm(instance=user)
    
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'tienda/profile.html', context)

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(request.session.get('previous_page', 'manage_usuarios'))
        else:
            return render(request, 'tienda/register.html', {'form': form, 'errors': form.errors})
    else:
        request.session['previous_page'] = request.META.get('HTTP_REFERER', 'manage_usuarios')
        form = RegistroForm()
    return render(request, 'tienda/register.html', {'form': form})