# -*- coding: utf-8 -*-


from django.contrib import admin
from coordinaAsignaturas.models import *

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Oferta)
admin.site.register(Inscripcion)
admin.site.register(Estudiante)
admin.site.register(Coordinador)
admin.site.register(Coordinacion)