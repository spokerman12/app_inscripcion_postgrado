# postgrado-NullPointerException
Repositorio del primer proyecto de Ingeniería de Software CI3715 de abril-julio 2018, Universidad Simón Bolívar.

Equipo: Null Pointer Exception

## Instrucciones basicas:

La página se llama "postgrado"
El app que cumple las historias se llama "coordinaAsignaturas"

1. Debemos clonar el repositorio, digamos en /home/
2. Entrar a /home/postgrado, 
	Si queremos visualizar la pagina, ejecutar (con Django instalado) `>python3 manage.py runserver`
		y entrar a `http://127.0.0.1:8000/` para vista de usuario (no funcional). 
		a `http://127.0.0.1:8000/admin` para vista de admin (funcional).

### Cuentas preparadas:

Administrador: admin | contrasena0000
Coordinador: postgradoCiencias@usb.ve | contrasena0000
Estudiante: 11-11111@usb.ve | contrasena0000

Permisología básica está implementada.
Mayores restricciones se implementarán a nivel de front-end.

## Estado actual Sprint 1:

Base de datos con objetos básicos y relaciones.
Más del 50% de las restricciones de campo se imponen a través de los modelos de Django.
Hace falta refinamiento pero es posible cumplir todas las historias de compromiso
a excepción de la 3.2, que requiere vistas.

## Orden de dependencias:

Profesor > Asignatura > Coordinacion > Coordinador > Oferta > Inscripcion > Estudiante

La pagina se llama "postgrado"
El app que cumple las historias se llama "coordinaAsignaturas"

1. Debemos clonar el repositorio, digamos en home/Proyecto
2. Dentro de home/Proyecto/postgrado, 
	Si queremos visualizar la pagina, ejecutar (con Django instalado) `>python3 manage.py runserver`
		y entrar a `http://127.0.0.1:8000/` para vista de usuario. Agregar `/admin` para vista de admin.

## Para actualizar el modelado de la base de datos
1. Cambiar modelos en models.py
2. Correr `>python3 manage.py makemigrations` para pasar Python a SQL (crear migraciones)
3. Correr `>python3 manage.py` migrate para ejecutar tales migraciones

[Documentacion de Django](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)