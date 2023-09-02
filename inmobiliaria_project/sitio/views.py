from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from .models import *
from .forms import UserRegisterForm, InicioSesionForm, ProfileUpdateForm, UserUpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#Vistas para el sitio - USERS

#- REGISTRO DE USUARIOS
def RegistroView(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if not User.objects.filter(username=request.POST.get('username')).exists():
            if not User.objects.filter(email=request.POST.get('email')).exists():
                if request.POST.get('password1') == request.POST.get('password2'):
                    username = request.POST.get('username')
                    email = request.POST.get('email')
                    password = request.POST.get('password1')
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    messages.success(request, f'Tu cuenta ha sido creada.')
                    return redirect('login')
                else:
                    messages.error(request, 'Las contraseñas no coinciden')
            else:
                messages.error(request, 'El email ya existe')
        else:
            messages.error(request, 'El usuario ya existe')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration/register.html', {'form': form})

#- LOGIN DE USUARIOS 
def LoginView(request):
    if request.method == "POST":
        form = InicioSesionForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Bienvenido ' + username)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales incorrectas')
        else:
            messages.error(request, 'Error al iniciar sesión. Intente nuevamente.')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'users/registration/login.html', context)


#- PERFIL DE USUARIO
@login_required
def PerfilView(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Tu perfil ha sido actualizado.')
            return redirect('perfil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html', context)


#RESTAURACION DE USUARIOS
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
    
#Vistas para SITIO

#PUBLICACION
@login_required
def PublicarView(request):
    return render(request,'sitio/publicacion.html')

#CONTACTO
def ContactoView(request):
    context = {}
    return render(request, 'contacto.html', context)

#HOME 
# def HomeView(request):
#     context = {
#         'publicaciones': Publicacion.objects.all()
#     }
#     return render(request, 'sitio/home.html', context)

### CRUD DE PPUBLICACIONES ###

#Listado de publicaciones -> Home
class PublicacionListView(ListView):
    model = Publicacion
    template_name = 'sitio/home.html'
    context_object_name = 'publicaciones'
    ordering = ['-fecha_actualizado']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Obtén los parámetros de búsqueda de la URL
        precio_min = self.request.GET.get('precio_min')
        precio_max = self.request.GET.get('precio_max')
        banos = self.request.GET.get('banos')
        habitaciones = self.request.GET.get('habitaciones')
        tipo_operacion = self.request.GET.get('tipo_operacion')
        tipo_propiedad = self.request.GET.get('tipo_propiedad')
        provincia = self.request.GET.get('provincia')
        ciudad = self.request.GET.get('ciudad')
        
        # Aplica los filtros solo si se proporcionan valores
        if precio_min:
            queryset = queryset.filter(precio__gte=precio_min)
        if precio_max:
            queryset = queryset.filter(precio__lte=precio_max)
        if banos:
            queryset = queryset.filter(banos=banos)
        if habitaciones:
            queryset = queryset.filter(habitaciones=habitaciones)
        if tipo_operacion:
            queryset = queryset.filter(tipo_operacion=tipo_operacion)
        if tipo_propiedad:
            queryset = queryset.filter(tipo_propiedad=tipo_propiedad)
        if provincia:
            queryset = queryset.filter(provincia__icontains=provincia)
        if ciudad:
            queryset = queryset.filter(ciudad__icontains=ciudad)

        return queryset

#Detalle de publicaciones
class PublicacionDetailView(DetailView):
    model = Publicacion

#Crear publicaciones
class PublicacionCreateView(LoginRequiredMixin, CreateView):
    model = Publicacion
    fields = ['titulo','descripcion','tipo_propiedad','tipo_operacion','precio','habitaciones','banos',
              'metros_cuadrados','direccion','provincia','ciudad','imagen_principal']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
#Editar publicaciones
class PublicacionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publicacion
    fields = ['titulo','descripcion','tipo_propiedad','tipo_operacion','precio','habitaciones','banos',
              'metros_cuadrados','direccion','provincia','ciudad','imagen_principal']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    #Codigo para evitar que cualquier usuario pueda editar publicaciones. 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context
    
    #Error 403 personalizado:
    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        
        post = self.get_object()
        return HttpResponseForbidden(
            f"No tienes permisos para editar esta publicación. <a href='{reverse('post-detail', args=[post.pk])}'>Volver atrás</a>"
        )

#Eliminar publicaciones
class PublicacionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publicacion
    success_url = '/'
    
    #Codigo para evitar que cualquier usuario pueda editar publicaciones. 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context
    
    #Error 403 personalizado:
    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        
        post = self.get_object()
        return HttpResponseForbidden(
            f"No tienes permisos para eliminar esta publicación. <a href='{reverse('post-detail', args=[post.pk])}'>Volver atrás</a>"
        )
    
    

