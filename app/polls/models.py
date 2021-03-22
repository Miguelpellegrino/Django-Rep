from django.db import models
from datetime import datetime
from .models import *

# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    CI = models.IntegerField(unique=True)
    nacimiento = models.DateField(default=datetime.now)
    edad = models.PositiveIntegerField("Edad")
    direccion = models.TextField("Direccion")
    entidad = models.ForeignKey("entidad",on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    

    class Meta:
        db_table = 'persona'

class entidad(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.TextField("")

    def __str__(self):
        return self.nombre
    

    class Meta:
        db_table = 'entidad'