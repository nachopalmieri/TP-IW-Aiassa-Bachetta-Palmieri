"""inmobiliaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from sitio import views

urlpatterns = [
    
    #Admin URLs
    path('admin/', admin.site.urls),
    #path('', include('sitio.urls')),
    path('', views.HomeView, name = 'home'),
    path('login/', views.LoginView, name = 'login'),
    path('logout/', views.LogoutView, name = 'logout'),
    path('registro/', views.RegistroView, name = 'register'),
    path('contacto/', views.ContactoView, name = 'contact'),
    
#URLS de la aplicacion de restaurar password
    path('reset_password/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/reset_password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/reset_password/password_reset_confirm.html'), name='password_reset_confirm'), 
    path('reset/password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/reset_password/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/', include('allauth.urls')),
]

