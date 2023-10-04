from django.shortcuts import render
from AppData.models import Curso
from AppData.forms import CursoFormulario 

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
            
            curso = Curso(nombre = informacion['curso'], comision = informacion['comision'])
            
            curso.save()
            
        return render(request, "AppData/index.html")
    
    else:
        
        miFormulario = CursoFormulario()
        
    return render(request, "AppData/apiCursoFormulario.html", {"miFormulario": miFormulario})


