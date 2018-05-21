from django.db import models

class Coordinacion(models.Model):
    nomCoord = models.CharField(max_length=40)
    codCoord = models.CharField(max_length=2, primary_key=True)

    def __str__(self):
        return self.nomCoord

class Usuario(models.Model):
    nomUsr = models.CharField(max_length=20, primary_key=True)
    claveUsr = models.CharField(max_length=16)
    codCoord = models.ForeignKey(Coordinacion, on_delete=models.PROTECT)

    TIPOUSR = (
        ('C','Coordinador'),
        ('E','Estudiante'),
    )
    tipoUsr = models.CharField(max_length=1, choices=TIPOUSR)

    def __str__(self):
        return self.nomUsr

class Oferta(models.Model):
    trimestre = models.CharField(max_length=10)
    anio = models.IntegerField()
    codCoord = models.ForeignKey(Coordinacion, on_delete=models.PROTECT)

    def __str__(self):
        return (str(self.trimestre)+" "+str(self.anio))

class Profesor(models.Model):
    ciProf = models.IntegerField(primary_key=True)
    nomProf = models.CharField(max_length=40)

    def __str__(self):
        return self.nomProf


class Asignatura(models.Model):
    codAsig = models.CharField(max_length=7, primary_key=True)
    codCoord = models.ForeignKey(Coordinacion, on_delete=models.PROTECT)
    creditos = models.IntegerField(default=0)
    nomAsig = models.CharField(max_length=40)
    progAsig = models.CharField(max_length=6)
    dia = models.CharField(max_length=10)
    horas = models.CharField(max_length=5)
    nomProf = models.CharField(max_length=30)
    ofertas = models.ManyToManyField(Oferta)
    ciProf = models.ForeignKey(Profesor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nomAsig

    class Meta:
        ordering = ('nomAsig',)

