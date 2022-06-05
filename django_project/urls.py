
from django.contrib import admin
from django.urls import path
from webapp.views import Bienvenido, Bienvenidorecursos
from personas.views import detallepersona , nuevapersona, editarpersona, eliminarpersona, nuevorecurso, eliminarrecurso, editarrecurso


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Bienvenido , name='index'),
  path('detalle_recurso', Bienvenidorecursos , name='recursos'),
    path('detallepersona/<int:id>', detallepersona ),
    path('nuevapersona', nuevapersona),
  path('nuevo_recurso', nuevorecurso),
  path('editar_persona/<int:id>', editarpersona),
  path('editar_recurso/<int:id>', editarrecurso),
  path('eliminar_persona/<int:id>', eliminarpersona),
  path('eliminar_recurso/<int:id>', eliminarrecurso),
]
