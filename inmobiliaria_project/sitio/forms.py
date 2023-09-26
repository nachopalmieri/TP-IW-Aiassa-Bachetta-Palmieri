#Formularios para el sitio
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Review

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