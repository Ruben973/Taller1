from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from Noticias.models import Noticias
from .forms import FormComentario

def vistaprincipal(request,noticia_id):
    noticia = get_object_or_404(Noticias, pk=noticia_id)
    comentario= FormComentario()
    return render(request,'noticias.html',{'noticia': noticia,'comentario': comentario})

# Create your views here.
