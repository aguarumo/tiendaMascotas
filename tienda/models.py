from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Producto(models.Model):
    categoria_choices = [
        ('alimentos', 'Alimentos'),
        ('exoticos', 'Exóticos'),
        ('farmacia', 'Farmacia'),
        ('juguetes', 'Juguetes'),
        ('limpieza', 'Limpieza'),
        ('ropa', 'Ropa'),
    ]

    titulo = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='media/imagenes/')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    detalle = models.TextField()
    stock = models.IntegerField()
    codigo = models.CharField(max_length=255)
    envio = models.BooleanField(default=True)
    retiro = models.BooleanField(default=True)
    categoria = models.CharField(max_length=20, choices=categoria_choices)

    def __str__(self):
        return self.titulo
    

class Usuario(AbstractUser):
  
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    rut = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username