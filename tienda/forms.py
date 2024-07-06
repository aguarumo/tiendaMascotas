from django import forms
from .models import  Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'titulo', 
            'imagen', 
            'descripcion', 
            'precio', 
            'detalle', 
            'stock', 
            'codigo', 
            'envio', 
            'retiro', 
            'categoria'
        ]
    
def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return codigo
        if Producto.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError("Este código ya existe.")
        
        return codigo