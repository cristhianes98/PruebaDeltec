from django.http import HttpResponse
from django.shortcuts import render
from personas.models import personas, recurso


def Bienvenido(request):
    n_personas = personas.objects.count()

    #l_personas = personas.objects.all()
    l_personas = personas.objects.order_by('id')
    return render(request, 'Inicio.html' , {'n_personas': n_personas, 'l_personas': l_personas})

def Bienvenidorecursos(request):
    n_recursos = recurso.objects.all()
    #l_personas = personas.objects.all()
    l_recursos = recurso.objects.order_by('id')
    return render(request, 'drecurso.html' , {'n_recursos': n_recursos, 'l_recursos': l_recursos,})