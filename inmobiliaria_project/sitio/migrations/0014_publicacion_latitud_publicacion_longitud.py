# Generated by Django 4.1.6 on 2023-09-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0013_review_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='latitud',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='longitud',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
