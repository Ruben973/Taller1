from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .forms import FormContacto

def vistacontacto(request):

    form=FormContacto()

    if request.POST:
        form=FormContacto(request.POST)

        if form.is_valid():

            asunto = form.cleaned_data['asunto']
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            dpto = form.cleaned_data['departamento']
            nc = form.cleaned_data['numerodecliente']
            cons = form.cleaned_data['consulta']
            mail(asunto, nombre, email, dpto, nc, cons)
        
            return render(request,'respuesta.html')
    return render(request,'paginaContacto.html',{'form': form})

def mail(asunto,nombre,desde,para,numerodecliente,cuerpo):
    
    print(locals()) 

    

# Create your views here.
