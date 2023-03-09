from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required


from django.urls import reverse, reverse_lazy
from .forms import *


# Create your views here.

def login_request(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form= AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            pw= form.cleaned_data.get('password')

            user= authenticate(username=usuario,password=pw)
            if user is not None:
                login(request,user)
                return render (request,'PostApp/inicio.html',{'mensaje':f'Bienvenido {usuario}'})
            else:
                return render (request, 'UserApp/login.html',{'mensaje':f'Error, datos incorrectos','form':form})
        else:
            return render (request, 'UserApp/login.html',{'mensaje':f'Error, datos incorrectos','form':form})
    else:
        return render(request,'UserApp/login.html',{'form':form})
    

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            #username = form.cleaned_data['username']
            form.save()
            return render(request,'PostApp/inicio.html', {'mensaje':'Usuario creado'})
        
    else:
        form=MyUserCreationForm()
    return render (request,'UserApp/registro.html',{'form':form})


@login_required
def editar_perfil(request):

    usuario = User.objects.get(username=request.user)

    if request.method == 'POST':
        form= UserEditForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            usuario.username=informacion['username']
            usuario.email=informacion['email']
            usuario.last_name=informacion['last_name']
            usuario.first_name=informacion['first_name']

            usuario.save()

            return redirect('/')
    else:
        form = UserEditForm(initial={'username':usuario.username,'email':usuario.email,'last_name':usuario.last_name,'first_name':usuario.first_name})

    contexto={'form':form,'usuario':usuario}
    return render (request,'UserApp/editar-usuario.html',contexto)


@login_required
def agregar_avatar(request):
    avatar=request.user.avatar
    form= AvatarFormulario(instance=avatar)
    if request.method == 'POST':
        form= AvatarFormulario(request.POST,request.FILES,instance=avatar)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        return render(request,'UserApp/agregar-avatar.html',{'form':form})
