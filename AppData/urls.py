from django.urls import path
from .views import inicio, cursos, tecnologias, opiniones, contacto, apiCursoFormulario, buscar, mostrar

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('tecnologias/', tecnologias, name="Tecnologias"),
    path('opiniones/', opiniones, name="Opiniones"),
    path('contacto/', contacto, name="Contacto"),
    path('apicursoform/', apiCursoFormulario, name="apiCursoForm"),
    path('buscar/', buscar, name="Buscar"),
    path('mostrar/', mostrar, name="Mostrar")
]
