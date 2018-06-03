

'''
python3 manage.py makemigrations coordinaAsignaturas
python3 manage migrate

'''
from coordinaAsignaturas.models import *
a = Usuario()
a.crearUsuario("cochino","frito")
a.save()
k = Coordinador()
k.usuario = a
c = Coordinacion()
c.nomCoord="ECO"
k.coordinacion=c
k.save()
c.save()
s = Sesion()
s.validaUsuario("cochino","frito")
s.save()
s.getCoordinacion()