from django.urls import path,include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('tienda_productos/', views.tienda_productos, name='tienda_productos'),
    path('tienda', views.tienda, name='tienda'),
    path('nosotros', views.nosotros, name='nosotros'),
]