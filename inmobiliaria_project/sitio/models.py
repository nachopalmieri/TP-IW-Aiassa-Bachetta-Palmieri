from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage  

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

    ESTADO = [
        ('pendiente', 'Pendiente'),
        ('publicada', 'Publicada'),
        ('rechazada', 'Rechazada'),
    ]
    
    estado = models.CharField(max_length=20, choices=ESTADO, default='pendiente')

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo_operacion = models.CharField(default='',max_length=10, choices=TIPO_OPERACION)
    tipo_propiedad = models.CharField(default='',max_length=20, choices=TIPO_PROPIEDAD)
    precio = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    habitaciones = models.PositiveIntegerField(default=1)
    ambientes = models.PositiveIntegerField(default=1)
    metros_cuadrados = models.PositiveIntegerField(default=1)
    direccion = models.CharField(default='', max_length=200)
    provincia = models.CharField(default='', max_length=200)
    ciudad = models.CharField(default='', max_length=200)
    imagen_principal = models.ImageField(default='propiedad_default1.jpg')
    image2 = models.ImageField(default='propiedad_default2.jpg')
    image3 = models.ImageField(default='propiedad_default3.jpg')
    image4 = models.ImageField(default='propiedad_default4.jpg')
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
    favoritos = models.ManyToManyField('Publicacion', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         user_profile = Profile(user=instance)
#         user_profile.save()

#post_save.connect(create_profile, sender=User)

def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)
    
    # After save, read the file
    image_read = storage.open(self.image.name, "r")
    image = Image.open(image_read)
    
    if image.height > 200 or image.width > 200:
        size = (200, 200)
        
        # Create a buffer to hold the bytes
        imageBuffer = BytesIO()
        
        # Resize  
        image.thumbnail(size, Image.ANTIALIAS)
        
        # Save the image as jpeg to the buffer
        image.save(imageBuffer, image.format)
        
        # Save the modified image
        user = User.objects.get(pk=self.pk)
        user.profile.image.save(self.image.name, ContentFile(imageBuffer.getvalue()))
        
        image_read = storage.open(user.profile.image.name, "r")
        image = Image.open(image_read)
        image.show()
        image_read.close()

class Review(models.Model):
    CHOICES = [
        ('Buena', 'Buena'),
        ('Regular', 'Regular'),
        ('Mala', 'Mala'),
    ]

    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=50, choices=CHOICES)
    description = models.TextField()

    def __str__(self):
        return f"Reseña realizada por {self.reviewer.username} para {self.reviewed_user.username}"








