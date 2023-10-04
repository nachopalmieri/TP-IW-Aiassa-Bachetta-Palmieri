#Formularios para el sitio
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Review, Publicacion

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class InicioSesionForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'description']
        
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'descripcion', 'tipo_propiedad', 'tipo_operacion', 'precio', 'expensas', 'habitaciones',
                  'metros_cuadrados', 'ambientes', 'banios', 'imagen_principal', 'image2', 'image3', 'image4', 'latitud', 'longitud', 'provincia', 'ciudad', 'direccion']
        
        provincia = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Provincia'}))
        ciudad = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}))
        direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dirección'}))
    
        widgets = {
            'latitud': forms.HiddenInput(),
            'longitud': forms.HiddenInput(),
        }
        
    banios = forms.IntegerField(label='Baños', initial=1)