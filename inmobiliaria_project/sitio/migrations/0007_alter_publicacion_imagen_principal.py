# Generated by Django 4.1.6 on 2023-09-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0006_rename_ubicacion_publicacion_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='imagen_principal',
            field=models.ImageField(default='propiedad_default.jpg', upload_to='propiedades'),
        ),
    ]