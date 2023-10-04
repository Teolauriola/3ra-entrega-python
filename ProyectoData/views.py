from django.http import HttpResponse
from django.template import Template, context
from django.template import loader

def inicio(request):
	return HttpResponse("Página de inicio - AppData <br>Bienvenidos")

def saludo(request):
	return HttpResponse("Hola Django - Coder <br>Hola Alumnos")
