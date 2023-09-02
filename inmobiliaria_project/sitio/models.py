from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.
#User._meta.get_field('email')._unique = True

class Publicacion(models.Model):
    TIPO_OPERACION = (
        ('venta', 'Venta'),
        ('alquiler', 'Alquiler'),
        ('temporada', 'Temporada')
    )
    
    TIPO_PROPIEDAD = (
        ('departamento','Departamento'),
        ('casa','Casa'),
        ('deposito','Deposito'),
        ('edificio','Edificio'),
        ('quinta','Quinta Vacacional')
    )

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo_operacion = models.CharField(default='',max_length=10, choices=TIPO_OPERACION)
    tipo_propiedad = models.CharField(default='',max_length=20, choices=TIPO_PROPIEDAD)
    precio = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    habitaciones = models.PositiveIntegerField(default=1)
    banos = models.PositiveIntegerField(default=1)
    metros_cuadrados = models.PositiveIntegerField(default=1)
    direccion = models.CharField(default='', max_length=200)
    provincia = models.CharField(default='', max_length=200)
    ciudad = models.CharField(default='', max_length=200)
    imagen_principal = models.ImageField(default='propiedad_default.jpg', upload_to='propiedades')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_actualizado = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         user_profile = Profile(user=instance)
#         user_profile.save()

#post_save.connect(create_profile, sender=User)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

