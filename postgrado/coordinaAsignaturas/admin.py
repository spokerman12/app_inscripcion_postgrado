# -*- coding: utf-8 -*-

'''
Se registran los models para manejarlos con el panel de administrador

'''


from django.contrib import admin
from coordinaAsignaturas.models import Profesor, Asignatura, Oferta, Sesion
from coordinaAsignaturas.models import Inscripcion, Estudiante, Coordinador
from coordinaAsignaturas.models import Coordinacion, Usuario

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Oferta)
admin.site.register(Inscripcion)
admin.site.register(Estudiante)
admin.site.register(Coordinador)
admin.site.register(Coordinacion)
admin.site.register(Usuario)
admin.site.register(Sesion)
