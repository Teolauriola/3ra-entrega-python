from django.http import HttpResponse
from django.template import Template, context, loader
from datetime import datetime as dt


def saludo(request):
	return HttpResponse("Hola Django - Coder <br>Hola Alumnos")
