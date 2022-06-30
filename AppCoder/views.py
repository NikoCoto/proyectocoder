from django.shortcuts import render

from AppCoder.models import Curso
from AppCoder.models import Curso
from django.http import HttpResponse    


# Create your views here.


def curso(self):

    curso=Curso(nombre="Django", comision=939393)
    curso.save()

    texto= f"Curso Creado: {curso.nombre} {curso.comision}"

    return HttpResponse(texto)



