from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import RegistroForm, InicioSesionForm 




#Vistas para el sitio

#Vista para el registro de usuarios
def RegistroView(request):
    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if not User.objects.filter(username=request.POST.get('username')).exists():
            if not User.objects.filter(email=request.POST.get('email')).exists():
                if request.POST.get('password1') == request.POST.get('password2'):
                    username = request.POST.get('username')
                    username = request.POST.get('username')
                    email = request.POST.get('email')
                    password = request.POST.get('password1')
                    user = User.objects.create_user(username, email, password)
                    user.save()

                    return redirect('login')
                else:
                    messages.error(request, 'Las contraseñas no coinciden')
            else:
                messages.error(request, 'El email ya existe')
        else:
            messages.error(request, 'El usuario ya existe')
    else:
        form = RegistroForm()
    return render(request, 'users/registration/register.html', {'form': form})

#Vista para el login de usuarios
def LoginView(request):
    if request.method == "POST":
        form = InicioSesionForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.success(request, 'Bienvenido ' + username)
                return HttpResponseRedirect("/")
            else:
                messages.error(request, 'Credenciales incorrectas')
        else:
            messages.error(request, 'Error al iniciar sesión. Intente nuevamente.')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'users/registration/login.html', context)

#Vistas para el logout de usuarios
def LogoutView(request):
    context = {}
    return render(request, 'users/registration/logout.html', context)

def ContactoView(request):
    context = {}
    return render(request, 'contacto.html', context)

def HomeView(request):
    context = {
        'publicaciones': Publicacion.objects.all()
    }
    return render(request, 'home.html', context)

@login_required
def PerfilView(request):
    return render(request,'users/profile.html')

@login_required
def PublicarView(request):
    return render(request,'publicacion.html')

#Vista con lo que se muestra en el mail de restauracion de contraseña
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/reset_password/password_reset.html'
    email_template_name = 'users/reset_password/password_reset_email.html'
    subject_template_name = 'users/reset_password/password_reset_subject.txt'

class CustomPasswordResetView(PasswordResetView):

    template_name = 'users/reset_password/password_reset.html'
    email_template_name = 'users/reset_password/password_reset_email.html'
    subject_template_name = 'users/reset_password/password_reset_subject.txt'

    protocol = 'https'  # Cambia esto según tu configuración
    domain = 'tulugar.onrender.com'  # Cambia esto a tu dominio real
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocol'] = self.protocol
        context['domain'] = self.domain
        return context

    