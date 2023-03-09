from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *



urlpatterns = [
    path('login/', login_request, name='login'),
    path('registro/', register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='UserApp/logout.html'), name='logout'),
    path('editar-perfil/', editar_perfil, name='editar-perfil'),
    path('agregar-avatar/', agregar_avatar, name='agregar-avatar'),


]