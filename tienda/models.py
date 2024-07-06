from django.db import models
from django.contrib.auth.models import abstractUser
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
    imagen = models.ImageField(upload_to='imagenes/')
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
    
class Usuario(abstractUser):
    
    usuario = models.CharField(max_length=255)
    nombre = models.TextField()
    rut = models.IntegerField()
    correo = models.TextField()
    telefono = models.IntegerField()
    direccion = models.TextField()

    def __str__(self):
        return self.usuario