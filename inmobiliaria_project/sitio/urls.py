from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

#URLS de la app
urlpatterns = [
    path('', views.HomeView, name = 'home'),
    path('login/', views.LoginView, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/registration/logout.html'), name = 'logout'),
    path('registro/', views.RegistroView, name = 'register'),
    path('perfil/', views.PerfilView, name = 'perfil'),
    path('publicar/', views.PublicarView, name = 'publicar'),
    path('contacto/', views.ContactoView, name = 'contact'),
    
#URLS de la aplicacion de restaurar password
    path('reset_password/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/reset_password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/reset_password/password_reset_confirm.html'), name='password_reset_confirm'), 
    path('reset/password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/reset_password/password_reset_complete.html'), name='password_reset_complete'),
]