from django.db import models

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    texto= models.TextField()
    def __str__(self):              # __unicode__ on Python 2
        return self.titulo


class Comentario(models.Model):
    fecha=models.DateTimeField()
    nombre=models.CharField(max_length=200)
    texto=models.TextField()
# Create your models here.
