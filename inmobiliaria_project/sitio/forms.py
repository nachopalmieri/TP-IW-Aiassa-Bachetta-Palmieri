#Formularios para el sitio
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InicioSesionForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    