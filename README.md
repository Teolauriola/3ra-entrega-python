# 3ra entrega - Proyecto Python (Django).

## Índice

- [3ra entrega - Proyecto Python (Django).](#3ra-entrega---proyecto-python-django)
  - [Índice](#índice)
  - [1.- Introducción.](#1--introducción)
  - [2.- Requisitos](#2--requisitos)
  - [3.- Instalación y Configuración](#3--instalación-y-configuración)
  - [4.- Uso](#4--uso)
  - [5.- Vistas](#5--vistas)
  - [6.- Funcionalidades](#6--funcionalidades)
  - [6.- Creador del proyecto](#6--creador-del-proyecto)

## 1.- Introducción.

Este proyecto tiene por finalidad poner a prueba el contenido aprendido durante la cursada, las utilidades que posee Django en lo que hace al desarrollo web y gestión de base de datos.

## 2.- Requisitos

- Python 3.12.0
- Django 4.2.6
- Db.sqlite3
  

## 3.- Instalación y Configuración

3.1.- **Clonar el Repositorio**
    
    git clone https://github.com/Teolauriola/3ra-entrega-python.git
    cd ./CoderHouse - Python/3ra Entrega - Python
    
**Es importante mencionar que debe hacerse los siguientes pasos para poder utilizar el último código:** 

    1.- Debe clonarse el repositorio con el link anterior. 
    2.- utilizamos el comando $ git ckeckout main. De esta manera se copiaran los archivos de la rama.
   

3.2.- **Configurar el entorno virtual**
    
    Para este proyecto se decidió no configurar un enterno virtual.
    

3.3.- **Instalar las dependencias**
    
    En cd ./CoderHouse - Python/3ra Entrega - Python pip install django.
    

3.4.- **Realizar las migraciones**
    
    En cd ./CoderHouse - Python/3ra Entrega - Python python manage.py migrate
    

## 4.- Uso

4.1.- **Iniciar el servidor de desarrollo**
    
    En cd ./CoderHouse - Python/3ra Entrega - Python python manage.py runserver
    

4.2.- **Abre tu navegador y navega a:** 
`http://127.0.0.1:8000/`

## 5.- Vistas

Se encontraran en total 7 vistas:
    - Inicio
    - Cursos
    - Tecnologías
    - Opiniones
    - Contacto
    - Formulario
    - Busqueda

**Nota**: Se utiliza herencia en el navbar y en el body del proyecto.La plantilla madre es plantilla_base.html

## 6.- Funcionalidades

6.1.- **Formulario**:
    - Esta página nos permite poder crear un formulario para insertar datos a todas las clases de models que tengamos en el proyecto

6.2.- **Busqueda**:
    - Esta página tiene la funcionalidad de que nos permite buscar cursos en nuestra base de datos.

## 6.- Creador del proyecto

**Este proyecto está siendo desarrollado por:**

- Nombre: Matteo Lauriola (Wninja.13)
