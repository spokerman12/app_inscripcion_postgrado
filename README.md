# posgrado-NullPointerException
Repositorio del primer proyecto de Ingeniería de Software CI3715 de abril-julio 2018, Universidad Simón Bolívar.

Equipo: Null Pointer Exception

## Instrucciones basicas:

La pagina se llama "postgrado"
El app que cumple las historias se llama "coordinaAsignaturas"

1. Debemos clonar el repositorio, digamos en home/Proyecto
2. Dentro de home/Proyecto/postgrado, 
	Si queremos visualizar la pagina, ejecutar (con Django instalado) `>python3 manage.py runserver`
		y entrar a `http://127.0.0.1:8000/` para vista de usuario. Agregar `/admin` para vista de admin.

Seguir [documentacion de Django](https://docs.djangoproject.com/en/2.0/intro/tutorial01/) en todo momento...!

## Para actualizar el modelado de la base de datos
1. Cambiar modelos en models.py
2. Correr `>python3 manage.py makemigrations` para pasar Python a SQL (crear migraciones)
3. Correr `>python3 manage.py` migrate para ejecutar tales migraciones