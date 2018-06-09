from coordinaAsignaturas.models import *
from manage import *

manage.makemigrations(coordinaAsignaturas)
manage.migrate()

a = coordinaAsignaturas.models.Usuario()
a.crearUsuario("cochino","frito")
a.save()
k = coordinaAsignaturas.models.Coordinador()
k.coordinador = a
k.save()
c = coordinaAsignaturas.models.Coordinacion("ECO")
c.save()
s = coordinaAsignaturas.models.Sesion()
s.validaUsuario("cochino","frito")
s.save()
s.getCoordinacion()
