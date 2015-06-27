from django import forms

class FormComentario(forms.Form):

    nombre=forms.CharField()
    edad=forms.IntegerField()
