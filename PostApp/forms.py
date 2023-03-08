from django import forms

class DirectoresFormulario(forms.Form):
    nombre=forms.CharField()
    obra=forms.CharField()


class PeliculaFormulario(forms.Form):
    nombre= forms.CharField()
    estreno= forms.IntegerField()
    direc= forms.CharField()
    genero=forms.CharField()


class ActoresFormulario(forms.Form):
    nombre= forms.CharField()
    edad= forms.IntegerField()
