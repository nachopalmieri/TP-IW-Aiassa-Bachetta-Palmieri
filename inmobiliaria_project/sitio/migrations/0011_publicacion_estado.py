# Generated by Django 4.1.6 on 2023-09-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0010_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('publicada', 'Publicada'), ('rechazada', 'Rechazada')], default='pendiente', max_length=20),
        ),
    ]
