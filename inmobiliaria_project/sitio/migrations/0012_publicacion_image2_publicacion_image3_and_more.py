# Generated by Django 4.1.6 on 2023-09-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0011_publicacion_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='image2',
            field=models.ImageField(default='propiedad_default2.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='image3',
            field=models.ImageField(default='propiedad_default3.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='image4',
            field=models.ImageField(default='propiedad_default4.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='imagen_principal',
            field=models.ImageField(default='propiedad_default1.jpg', upload_to=''),
        ),
    ]
