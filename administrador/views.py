from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def menu(request):
    request.session["usuario"]="acoy"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(context, 'administrador/menu.html', context)

def home(request):
    context = {}
    return render(request, 'administrador/home.html', context)