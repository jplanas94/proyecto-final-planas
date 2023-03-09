from django.urls import path
from .views import *



urlpatterns = [
    path('', inicio, name='inicio'),
    #path('actores/', actores, name='actores'),
    path('directores/', directores, name='directores'),
    path('buscar/', buscar, name='buscar'),
    path('agregar-pelicula/', agregar_peliculas, name='agregar-pelicula'),
    path('leer-peliculas/', leer_peliculas, name='leer-peliculas'),
    path('eliminar-pelicula/<pelicula_id>', eliminar_pelicula,name='eliminar-pelicula'),
    path('editar-pelicula/<pelicula_id>', editar_pelicula,name='editar-pelicula'),
    path('actores-list/',ActoresList.as_view(), name='actores-list'),
    path('actores-detalle/<pk>',ActoresDetalle.as_view(), name='actores-detalle'),
    path('actores-nuevo/',ActoresCrear.as_view(), name='actores-nuevo'),
    path('actores-update/<pk>',ActoresUpdate.as_view(), name='actores-update'),
    path('actores-eliminar/<pk>',ActoresDelete.as_view(), name='actores-eliminar'),

]