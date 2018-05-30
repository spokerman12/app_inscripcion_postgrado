'''
Universidad Simón Bolívar (USB)
Ingeniería de Software I - CI3715
Equipo Null Pointer Exception
Configuración de panel de administrador de Django

'''

from django.contrib import admin
from coordinaAsignaturas.models import *

# Registre los modelos aquí
admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Oferta)
admin.site.register(Inscripcion)
admin.site.register(Estudiante)
admin.site.register(Coordinador)
admin.site.register(Coordinacion)