from django.contrib import admin

from .models import Producto,Usuario,Categoria

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Usuario)
