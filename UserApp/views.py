from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate


from django.urls import reverse, reverse_lazy
from .forms import MyUserCreationForm

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
            username = form.cleaned_data['username']
            form.save()
            return render(request,'PostApp/inicio.html', {'mensaje':'Usuario creado'})
        
    else:
        form=MyUserCreationForm()
        return render (request,'UserApp/registro.html',{'form':form})
