# Generated by Django 4.1.6 on 2023-09-28 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0014_publicacion_latitud_publicacion_longitud'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='expensas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
