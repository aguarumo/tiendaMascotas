from django.urls import path,include
from . import views

urlpatterns = [
    path('menu', views.menu, name='menu'),
   
    path('home', views.home, name='home'),


]