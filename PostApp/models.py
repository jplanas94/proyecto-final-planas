from django.db import models

# Create your models here.


class pelicula(models.Model):
    nombre= models.CharField(max_length=40)
    estreno= models.IntegerField()
    direc= models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre+ '(' + str(self.estreno) + ')'


class actor(models.Model):
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    def __str__(self):
        return self.nombre
    
    class meta:
        verbose_name_plural='Actores'

class director(models.Model):
    nombre= models.CharField(max_length=40)
    obras= models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre    
    
    class meta:
        verbose_name_plural='Directores'