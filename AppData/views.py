from django.http import HttpResponse
from django.shortcuts import render
from AppData.models import Curso
from AppData.forms import CursoFormulario, BuscaCursoForm

# Create your views here.
def inicio(request):
	return render(request, "AppData/index.html")

def cursos(request):
    return render(request, "AppData/cursos.html")

def opiniones(request):
	return render(request, "AppData/opiniones.html")

def tecnologias(request):
    return render(request, "AppData/tecnologias.html")

def contacto(request):
    return render(request, "AppData/contacto.html")

def apiCursoFormulario(request):
    
    if request.method == 'POST':
        
        miFormulario = CursoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            curso = Curso (curso=informacion["curso"], comisión=informacion["comisión"], turno=informacion["turno"])
            
            curso.save()
            
        return render(request, "AppData/index.html")
    
    else:
        
        miFormulario = CursoFormulario()
        print(miFormulario)
        
    return render(request, "AppData/apiCursoFormulario.html", {"miFormulario": miFormulario})

def buscar(request):
    
    if request.method == 'POST':
        
        miFormulario = BuscaCursoForm(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(curso__icontains=informacion["curso"])
            
        return render(request, "AppData/lista.html", {"cursos": cursos})
    
    else:
        
        miFormulario = BuscaCursoForm()
        print(miFormulario)
        
    return render(request, "AppData/buscar.html", {"miFormulario": miFormulario})

def mostrar(request):
    pass
