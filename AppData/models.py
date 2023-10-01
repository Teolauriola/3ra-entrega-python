from django.db import models

# Create your models here.
class Curso(models.Model):
    curso = models.CharField(max_length=30)
    comisión = models.IntegerField()
    turno = models.CharField(max_length=20)
    
    
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    pais = models.CharField(max_length=20)
    email = models.EmailField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    email = models.EmailField()