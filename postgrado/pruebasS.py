'''

Pruebas de Shell

python3 manage.py makemigrations coordinaAsignaturas
python3 manage migrate

'''
from coordinaAsignaturas.models import *

p = Profesor()
p.ciProf = 123
p.nomProf = "Farith"
p.save()
c = Coordinacion()
c.nomCoord = "MAT"
c.agregaAsignaturaNueva("MA-1111","MA",4,"Matematicas I","Derivadas","Lunes 3-4",123)
c.obtenAsignatura("MA-1111")
c.obtenAsignaturas()