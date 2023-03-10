# Generated by Django 4.1.7 on 2023-03-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('obras', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('estreno', models.IntegerField()),
                ('direc', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=40)),
            ],
        ),
    ]
