# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

fecha = datetime.datetime.now()


DPTOS = (
    ('EA','Estudios Ambientales'),
    ('CE','Ciencias Económicas y Administrativas'),
    ('CC','Ciencia y Tecnología del Comportamiento'),
    ('FIS','Física'),
    ('QM','Química'),
    ('MC','Mecánica'),
    ('MA','Matemáticas Puras y Aplicadas'),
    ('CI','Computación y Ciencias de la Información'),
    ('CO','Cómputo Científico y Estadística'),
    ('EC','Electrónica y Circuitos'),
    ('TF','Termodinámica y Fenómenos de Transferencia'),
    ('PS','Procesos y Sistemas'),
    ('MT','Ciencias de los Materiales'),
    ('GC','Ciencias de la Tierra'),
    ('LL','Lengua y Literatura'),
    ('ID','Idiomas'),
    ('FLX','Filosofía'),
    ('CS','Ciencias Sociales'),
    ('DA','Diseño Arquitectura y Artes Plásticas'),
    ('PL','Planificación Urbana'),
    ('BC','Biología Celular'),
    ('EA','Estudios Ambientales'),
    ('BO','Biología de Organismos'),
    ('PB','Tecnología de Procesos Biológicos y Bioquímicos'),
    )

COORDS = (
    ('BASICO','Ciclo Básico'),
    ('EGE','Ciclo Profesional'),
    ('GENERALES','Formación General'),
    ('CIU','Ciclo de Iniciación Universitaria'),
    ('QM','Química'),
    ('MAT','Matemática'),
    ('BIO','Biología'),
    ('FIS','Física'),
    ('EL','Tecnología e Ingeniería Eléctrica'),
    ('IE','Tecnología e Ingeniería Electrónica'),
    ('MEC','Ingeniería Mecánica'),
    ('IQ','Ingeniería Química'),
    ('CI','Ingeniería de Computación'),
    ('GC','Ingeniería Geofísica'),
    ('MTR','Ingeniería de Materiales'),
    ('PROD','Ingeniería de Producción y Organización Empresarial'),
    ('TMMA','Tecnología Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento'),
    ('IT','Ingeniería de Telecomunicaciones'),
    ('ARQ','Arquitectura'),
    ('URB','Estudios Urbanos'),
    ('TUR','Turismo, Hotelería y Hospitalidad'),
    ('EXT','Comercio Exterior y Licenciatura en Comercio Internacional'),
    ('P-CBA','Postgrado - Ciencias Básicas y Aplicadas'),
    ('P-CSH','Postgrado - Ciencias Sociales y Humanidades'),
    ('P-IT','Postgrado - Ingeniería y Tecnología'),
    )

TRIMESTRES   = (('E-M','Enero-Marzo'),('A-J','Abril-Julio'),('S-D','Septiembre-Diciembre'))


class Coordinador(models.Model):
    codCoord    = models.CharField(max_length=7, choices = COORDS)
    usuario     = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Coordinadores"

    
class Profesor(models.Model):
    ciProf      = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(99999999)])
    nomProf     = models.CharField(max_length=40)

    def __str__(self):
        return self.nomProf

    class Meta:
        verbose_name_plural = "Profesores"

class Asignatura(models.Model):
    codAsig     = models.CharField(max_length=7)
    codDpto     = models.CharField(max_length=6, choices = DPTOS)
    creditos    = models.IntegerField(choices = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),
                                                (7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15)))
    nomAsig     = models.CharField(max_length=80)
    progAsig    = models.CharField(max_length=20)
    dia         = models.CharField(max_length=20)
    horas       = models.CharField(max_length=10)
    prof        = models.ForeignKey(Profesor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nomAsig

    class Meta:
        ordering = ('nomAsig',)


class Oferta(models.Model):
    codCoord    = models.CharField(max_length=7, choices = COORDS)
    trimestre   = models.CharField(max_length=7, choices = TRIMESTRES)
    asignaturas = models.ManyToManyField(Asignatura)
    anio        = models.IntegerField(validators=[MinValueValidator(fecha.year),MaxValueValidator(2050)])

    def __str__(self):
        return (str(self.trimestre)+" "+str(self.anio))

    class Meta:
        ordering = ('anio',)


class Inscripcion(models.Model):
    asignaturas = models.ManyToManyField(Asignatura)
    anio        = models.IntegerField(validators=[MinValueValidator(fecha.year),MaxValueValidator(2050)])
    trimestre   = models.CharField(max_length=7, choices=TRIMESTRES)

    def __str__(self):
        return (self.trimestre+", "+str(self.anio))

    def sumCreditos(self):
        suma = 0
        for a in self.asignaturas:
            suma += a.creditos
        return (suma)

    class Meta:
        verbose_name_plural = "Inscripciones"

class Estudiante(models.Model):
    usuario         = models.OneToOneField(User, on_delete=models.CASCADE)
    carnet          = models.CharField(max_length=12)
    inscripciones   = models.ManyToManyField(Inscripcion)