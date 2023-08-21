from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
#User._meta.get_field('email')._unique = True

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    
