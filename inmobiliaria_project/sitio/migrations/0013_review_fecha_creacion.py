# Generated by Django 4.1.6 on 2023-09-27 23:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0012_publicacion_image2_publicacion_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]