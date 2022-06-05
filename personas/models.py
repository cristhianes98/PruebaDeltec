from django.db import models


class recurso(models.Model):
  categoria = models.CharField(max_length=10)
  codigo =  models.CharField(max_length=10)
  nombre = models.CharField(max_length=10)
  marca = models.CharField(max_length=10)
  serie =  models.CharField(max_length=3)

  def __str__(self):
    return f'recurso {self.id}: {self.categoria} {self.codigo} {self.nombre} {self.marca} {self.serie}'

class personas(models.Model):
  identificacion = models.CharField(max_length=9)
  nombre = models.CharField(max_length=255)
  apellido = models.CharField(max_length=255)
  recurso = models.ForeignKey(recurso, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return f'personas {self.id}: {self.identificacion} {self.nombre} {self.apellido} {self.recurso}'

