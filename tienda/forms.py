from django import forms
from .models import  Producto,Usuario,Profile,Categoria


class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Seleccione una categoría")

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
        if self.instance.pk:
            return codigo
        if Producto.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError("Este código ya existe.")
        return codigo

class RegistroForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    category = forms.ChoiceField(label='Categoría', choices=[('admin', 'Administrativo'), ('client', 'Cliente')])
    rut = forms.CharField(label='RUT', required=False)
    telefono = forms.CharField(label='Teléfono', required=False)
    direccion = forms.CharField(label='Dirección', required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'category', 'rut', 'nombre', 'apellido', 'telefono', 'direccion')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            self.add_error('password2', "Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if self.cleaned_data['category'] == 'admin':
            user.is_staff = True
        else:
            user.is_staff = False
        user.rut = self.cleaned_data['rut']
        user.nombre = self.cleaned_data['nombre']
        user.apellido = self.cleaned_data['apellido']
        user.telefono = self.cleaned_data['telefono']
        user.direccion = self.cleaned_data['direccion']
        if commit:
            user.save()

            Profile.objects.update_or_create(user=user)
        return user
    
class ActualizacionUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nombre', 'apellido', 'rut', 'telefono', 'direccion')

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'rut', 'telefono', 'direccion')
