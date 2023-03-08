from django.shortcuts import render



from PostApp.models import *
from .forms import *

# Create your views here.

def inicio (request):
    return render(request,'PostApp/inicio.html')

def leer_peliculas(request):
    mis_pelis=pelicula.objects.all()
    contexto={'mispelis':mis_pelis}
    return render(request,'PostApp/leer-peliculas.html',contexto)

def eliminar_pelicula(request, pelicula_id):
    peli=pelicula.objects.get(id=pelicula_id)
    peli.delete()

    mis_pelis=pelicula.objects.all()
    contexto= {'mispelis':mis_pelis}

    return render(request, 'PostApp/leer-peliculas.html', contexto)

def editar_pelicula(request, pelicula_id):
    peli=pelicula.objects.get(id=pelicula_id)

    if request.method == 'POST':
        mi_formulario = PeliculaFormulario(request.POST)

        #print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            peli.nombre= informacion['nombre']
            peli.estreno= informacion['estreno']
            peli.direc= informacion['direc']
            peli.genero= informacion['genero']
            peli.save()

            mis_pelis=pelicula.objects.all()
            contexto={'mispelis':mis_pelis}
            return render (request, 'PostApp/leer-peliculas.html', contexto)
    else:
        mi_formulario=PeliculaFormulario(initial={'nombre':peli.nombre,'estreno':peli.estreno,'direc':peli.direc,'genero':peli.genero})
        contexto = {'mi_formulario':mi_formulario, 'pelicula_id':pelicula_id}
        return render(request,'PostApp/editar-pelicula.html', contexto)


def agregar_peliculas (request):
    mis_peliculas=pelicula.objects.all()

    if request.method == 'POST':
        mi_formulario = PeliculaFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            peli= pelicula(nombre=informacion['nombre'], estreno=informacion['estreno'], direc=informacion['direc'], genero=informacion['genero'])
            peli.save()
            nueva_peli = {'nombre': informacion['nombre'], 'FechaDeEstreno':informacion['estreno'], 'direc':informacion['direc'], 'genero':informacion['genero']}
            return render (request, 'PostApp/agregar-pelicula.html',{'peliculaformulario': mi_formulario,'nueva_peli':nueva_peli,"mis_pelis":mis_peliculas })
    else:
        mi_formulario=PeliculaFormulario()

    return render(request,'PostApp/agregar-pelicula.html', {'peliculaformulario':mi_formulario,'mis_pelis':mis_peliculas})
   

def actores (request):
    mis_actores=actor.objects.all()


    if request.method == 'POST':
        mi_formulario = ActoresFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            act= actor(nombre=informacion['nombre'], edad=informacion['edad'])
            act.save()
            nuevo_actor={'nombre': informacion['nombre'], 'edad':informacion['edad']}
            return render (request, 'PostApp/actores.html',{'actoresformulario': mi_formulario,'nuevo_actor':nuevo_actor,"mis_actores":mis_actores })
    else:
        mi_formulario=ActoresFormulario()
    return render(request, 'PostApp/actores.html', {'actoresformulario':mi_formulario, 'mis_actores':mis_actores})


def directores (request):
    mis_directores = director.objects.all()

    if request.method == 'POST':
        mi_formulario = DirectoresFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            direc= director(nombre=informacion['nombre'], obras=informacion['obra'])
            direc.save()
            nuevo_director={'nombre': informacion['nombre'], 'obras':informacion['obra']}
            return render (request, 'PostApp/directores.html',{'directoresformulario': mi_formulario,'nuevo_director':nuevo_director,"mis_directores":mis_directores })
    else:
        mi_formulario=DirectoresFormulario()
    return render(request, 'PostApp/directores.html',{'directoresformulario':mi_formulario, 'mis_directores':mis_directores})
      

def busqueda_pelicula(request):
    return render(request, 'PostApp/inicio.html')

def buscar(request):
    if request.GET["fechadeestreno"]:
        FdE= request.GET["fechadeestreno"]
        resultado=pelicula.objects.filter(estreno__icontains = FdE)

        return render (request, 'PostApp/inicio.html',{'Peliculas':resultado, 'Fechadeestreno':FdE})
    else:
        respuesta='no se encontraron estrenos ese año'
    return render(request, 'PostApp/inicio.html',{'respuesta':respuesta})

