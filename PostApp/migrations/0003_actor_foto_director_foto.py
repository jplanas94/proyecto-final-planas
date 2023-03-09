# Generated by Django 4.1.7 on 2023-03-09 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0002_pelicula_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='actor'),
        ),
        migrations.AddField(
            model_name='director',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='director'),
        ),
    ]
