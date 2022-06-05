from django.shortcuts import render, redirect
from personas.models import personas, recurso
from django.forms import modelform_factory

# Create your views here.
def detallepersona(request, id):
  persona = personas.objects.get(pk=id)
  return render(request,'personas/detalle.html',{'persona':persona})




personaform = modelform_factory(personas, exclude=[])

def nuevapersona(request):
  if request.method == 'POST':
    formapersona = personaform(request.POST)
    if formapersona.is_valid():
      formapersona.save ()
      return redirect('index')
  else:
      formapersona = personaform()
      return render(request, 'personas/nuevo.html',     {'formapersona': formapersona})

recursoform = modelform_factory(recurso, exclude=[])

def nuevorecurso(request):
  if request.method == 'POST':
    formarecurso = recursoform(request.POST)
    if formarecurso.is_valid():
       formarecurso.save ()
       return redirect('index')
  else:
     formarecurso = recursoform()
     return render(request, 'personas/recurso.html',     {'formarecurso': formarecurso})

def editarpersona(request, id):
  persona = personas.objects.get(pk=id)
  if request.method == 'POST':
    formapersona = personaform(request.POST, instance=persona)
    if formapersona.is_valid():
      formapersona.save ()
      return redirect('index')
  else:
      formapersona = personaform(instance=persona)
      return render(request, 'personas/nuevo.html',     {'formapersona': formapersona})

recursoform = modelform_factory(recurso, exclude=[])

def editarrecurso(request, id):
  recursos = recurso.objects.get(pk=id)
  if request.method == 'POST':
    formarecurso = recursoform(request.POST, instance=recursos)
    if formarecurso.is_valid():
      formarecurso.save ()
      return redirect('recursos')
  else:
      formarecurso = recursoform(instance=recursos)
      return render(request, 'personas/editarrecurso.html',     {'formarecurso': formarecurso})




def eliminarpersona(request, id):
  persona = personas.objects.get(pk=id)
  if persona:
    persona.delete()
    return redirect('index')

def eliminarrecurso(request, id):
  recursos = recurso.objects.get(pk=id)
  if recursos:
    recursos.delete()
    return redirect('recursos')

