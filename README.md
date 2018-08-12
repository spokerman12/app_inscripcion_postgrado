# postgrado-NullPointerException
Repositorio del primer proyecto de Ingeniería de Software CI3715 de abril-julio 2018, Universidad Simón Bolívar.

Equipo: Null Pointer Exception

André Corcuera 12-10660
Daniel Francis 12-10863
Francisco Márquez 12-11163
Natascha Gamboa 12-111250
Ángel Morante 13-10931
Leonardo López 14-10576

## Instrucciones basicas:

La página se llama "postgrado"
El app que cumple las historias se llama "coordinaAsignaturas"

1. Debemos clonar el repositorio, digamos en /home/
2. Entrar a /home/postgrado, 
	Si queremos visualizar la pagina, ejecutar (con Django instalado) `>python3 manage.py runserver`
		y entrar a `http://127.0.0.1:8000/` para vista de usuario y 
		a `http://127.0.0.1:8000/admin` para vista de admin.

### Cuentas preparadas:

Para el panel de admin de Django:
Administrador: admin | contrasena0000

Para el sistema de asignaturas:

Coordinador: coord@usb.ve | ciencias
Estudiante: 11-11111@usb.ve | estudiante

La cuenta de estudiante aún no está habilitada.

Los nuevos usuarios deben ser creados a traves del metodo correspondiente en el modelo Sesion. Los usuarios no son los de Django.

## Estado actual Sprint 3:

Épicas 1, 2 y 3 listas a excepción de la descarga de ofertas en PDF.


## Cuando se cambian los modelos en models.py...

2. Correr `>python3 manage.py makemigrations` para pasar Python a SQL (crear migraciones)
3. Correr `>python3 manage.py` migrate para ejecutar tales migraciones

[Documentacion de Django](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)