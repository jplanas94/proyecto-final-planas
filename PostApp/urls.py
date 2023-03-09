from django.urls import path
from .views import *



urlpatterns = [
    path('', inicio, name='inicio'),
    #path('actores/', actores, name='actores'),
    #path('agregar-portada/', agregar_portada, name='agregar-portada'),
    path('buscar/', buscar, name='buscar'),
    path('agregar-pelicula/', PeliculasCrear.as_view(), name='agregar-pelicula'),
    path('leer-peliculas/', LeerPeliculas.as_view(), name='leer-peliculas'),
    path('pelicula-eliminar/<pk>', peliculasDelete.as_view(),name='pelicula-eliminar'),
    path('editar-pelicula/<pk>', PeliculasUpdate.as_view(),name='editar-pelicula'),
    path('peliculas-detalle/<pk>',PeliculasDetalle.as_view(), name='peliculas-detalle'),
    path('actores-list/',ActoresList.as_view(), name='actores-list'),
    path('actores-detalle/<pk>',ActoresDetalle.as_view(), name='actores-detalle'),
    path('actores-nuevo/',ActoresCrear.as_view(), name='actores-nuevo'),
    path('actores-update/<pk>',ActoresUpdate.as_view(), name='actores-update'),
    path('actores-eliminar/<pk>',ActoresDelete.as_view(), name='actores-eliminar'),
    path('directores-list/',DirectoresList.as_view(), name='directores-list'),
    path('directores-detalle/<pk>',DirectoresDetalle.as_view(), name='directores-detalle'),
    path('directores-nuevo/',DirectoresCrear.as_view(), name='directores-nuevo'),
    path('directores-update/<pk>',DirectoresUpdate.as_view(), name='directores-update'),
    path('directores-eliminar/<pk>',DirectoresDelete.as_view(), name='directores-eliminar'),


]