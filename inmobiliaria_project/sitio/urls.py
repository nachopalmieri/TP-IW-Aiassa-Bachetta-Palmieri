from django.contrib import admin
from . import views
from .views import PublicacionListView, PublicacionDetailView, PublicacionCreateView, PublicacionUpdateView, PublicacionDeleteView
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

#URLS de la app
urlpatterns = [
    path('', PublicacionListView.as_view(), name = 'home'),
    path('propiedad/<int:pk>/', PublicacionDetailView.as_view(), name = 'post-detail'),
    path('propiedad/nueva/', PublicacionCreateView.as_view(), name = 'post-create'),
    path('propiedad/<int:pk>/editar/', PublicacionUpdateView.as_view(), name = 'post-update'),
    path('propiedad/<int:pk>/eliminar/', PublicacionDeleteView.as_view(), name = 'post-delete'),
    path('login/', views.LoginView, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/registration/logout.html'), name = 'logout'),
    path('registro/', views.RegistroView, name = 'register'),
    path('perfil/', views.PerfilView, name = 'perfil'),
    #path('publicar/', views.PublicarView, name = 'publicar'),
    path('contacto/', views.ContactoView, name = 'contact'),

    path('accounts/profile/', views.PerfilView, name='profile'),

    path('favoritos/', views.MisFavoritosView, name='ver_favoritos'),
    path('toggle_favorito/<int:pk>/', views.FavoritosView, name='toggle_favorito'),
    path('ver_perfil/<int:user_id>/', views.VerPerfilView, name='ver_perfil'),


#URLS de la aplicacion de restaurar password
    path('reset_password/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/reset_password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/reset_password/password_reset_confirm.html'), name='password_reset_confirm'), 
    path('reset/password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/reset_password/password_reset_complete.html'), name='password_reset_complete'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
