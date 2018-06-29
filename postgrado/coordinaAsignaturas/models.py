# -*- coding: utf-8 -*-

'''
Universidad Simón Bolívar (USB)
Ingeniería de Software I - CI3715
Equipo Null Pointer Exception
Modelos para la aplicación coordinaAsignaturas

Ver modelo UML e informe técnico para mayor información

 Indice de modelos:
      1. Variables Globales.
        1.1. FECHA.
        1.2. DPTOS.
        1.3. COORDS.
        1.4. TRIMESTRES.
        1.5. CREDITOS.
      2. Clases.
        2.1. Usuario.
        2.2. Profesor.
        2.3. Asignatura.
        2.4. Coordinacion.
        2.5. Coordinador.
        2.6. Oferta.
        2.7. Inscripcion.
        2.8. Estudiante.
        2.9. Sesion.
      3. Funciones.
        3.1. obtenAsignaturas.
        3.2. buscaAsignaturas.
        3.3. eliminaAsignatura.
        3.4. eliminaOferta.
        3.5. eliminaAsignaturaDeCoord.
        3.6. agregaAsignaturaACoord.
        3.7. esEstudiante.
'''

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime, hashlib

'''
Fecha del acceso a la aplicación.
'''
FECHA = datetime.datetime.now()

'''
Departamentos de la USB junto a sus abreviaciones.
'''
>>>>>>> origin/H4-comentarios-Francisco
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

'''
Coordinaciones de postgrado de la USB junto a sus abreviaciones.
'''
>>>>>>> origin/H4-comentarios-Francisco
COORDS = (
    ('MAT','Matemáticas'),
    ('CB','Ciencias Biológicas'),
    ('CI','Ciencias de la Computación'),
    ('CAN','Ciencias de los Alimentos y Nutrición'),
    ('FIS','Física'),
    ('QM','Química'),
    ('DIC','Doctorado Interdisciplinario en Ciencias'),
    ('CP', 'Ciencia Política'),
    ('DYA', 'Desarrollo y Ambiente'),
    ('EDU', 'Educación'),
    ('EH', 'Estudios Humanos'),
    ('FLX', 'Filosofía'),
    ('EGE','Estudios en Gerencia y Economía'),
    ('LA','Lingüística Aplicada'),
    ('LIT','Literatura'),
    ('MUS','Música'),
    ('PSI','Psicología'),
    ('EXT','Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional'),
    ('DEI','Doctorado en Ingeniería'),
    ('ECO','Estadística Computacional'),
    ('IE','Ingeniería Electrónica'),
    ('IT','Ingeniería y Tecnología Eléctrica'),
    ('GC','Ingeniería Geofísica'),
    ('IM','Ingeniería Mecánica/Civil'),
    ('IQ','Ingeniería Química'),
    ('MTR','Ingeniería de Materiales'),
    ('IS','Ingeniería de Sistemas'),
    ('ITB','Ingeniería de Telecomunicaciones/Biomédica'),
    ('P-CBA','Postgrado - Ciencias Básicas y Aplicadas'),
    ('P-CSH','Postgrado - Ciencias Sociales y Humanidades'),
    ('P-IT','Postgrado - Ingeniería y Tecnología'),
    )

'''
Los tres períodos trimestrales estándar de la USB.
'''
TRIMESTRES   = (
    ('Ene-Mar','Enero-Marzo'),
    ('Abr-Jul','Abril-Julio'),
    ('Sept-Dic','Septiembre-Diciembre')
    )

'''
El numero de creditos posibles para una asignatura.
'''
CREDITOS = (
    (0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9),
    (10,10), (11,11), (12,12), (13,13), (14,14), (15,15)
    )

'''
Las clases descritas a continuación siguen el orden de dependencia igual al 
que poseen actualmente. Modificar con cuidado
'''
>>>>>>> origin/H4-comentarios-Francisco

'''
Clase que representa la entidad Usuario del sistema de postgrado.
'''
class Usuario(models.Model):
    username  = models.EmailField(max_length = 30, primary_key = True)
    password  = models.CharField(max_length = 64, null = False)
    nombres   = models.CharField(max_length = 80)
    apellidos = models.CharField(max_length = 80)

    '''
    Funcion que crea un usuario en la base de datos.
    usr -> Nombre de usuario
    pwd -> Contraseña
    Retorna True si se crea exitosamente, sino False
    '''
    def crearUsuario(self, usr, pwd):
        try:
            self.username = usr
            hashm = hashlib.sha256()
            pswd = str.encode(pwd)
            hashm.update(pswd)
            self.password = hashm.hexdigest()
            self.save()
            return True
        except:
            return False

    '''
    Extrae por defecto el nombre de usuario
    '''
    def __str__(self) -> str:
>>>>>>> origin/H4-comentarios-Francisco
        return self.username

    class Meta:
        app_label = 'coordinaAsignaturas'

'''
Clase que representa la entidad Profesor de la USB.
'''
>>>>>>> origin/H4-comentarios-Francisco
class Profesor(models.Model):
    ciProf  = models.IntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(99999999)],
        primary_key = True
        )
    nomProf = models.CharField(max_length = 80)

    def __str__(self) -> str:
        return self.nomProf

    class Meta:
        verbose_name_plural = "Profesores"
        app_label = 'coordinaAsignaturas'

>>>>>>> origin/H4-comentarios-Francisco

'''
Clase que representa la entidad Asignatura de postgrado. El campo diaHora
recibe restricciones de formato (e.g. "Lunes 7-8, Martes 5-6") a través de la
interfaz gráfica.
'''
class Asignatura(models.Model):
    codAsig  = models.CharField(max_length = 7, primary_key = True)
    codDpto  = models.CharField(max_length = 6, choices = DPTOS, blank = True)
    creditos = models.IntegerField(choices = CREDITOS)
    nomAsig  = models.CharField(max_length = 80, blank = True)
    progAsig = models.CharField(max_length = 20, blank = True)
    diaHora  = models.CharField(max_length = 60, blank = True)
    prof     = models.ForeignKey(Profesor, on_delete = models.PROTECT)
    vista    = models.BooleanField(default = False)

    '''
    Extrae por defecto el nombre de la asignatura.
    '''
    def __str__(self):
        return self.nomAsig

    class Meta:
        ordering = ('nomAsig',)
        app_label = 'coordinaAsignaturas'

    '''
    Elimina una asignatura de la base de dato. Retorna True si se elimina
    exitosamente, sino Flase
    '''
>>>>>>> origin/H4-comentarios-Francisco
    def eliminarAsignatura(self):
        try:
            return self.delete()
        except:
            return False

    '''
    Funcion que obtiene una asignatura de la base de datos. Retorna True si se
    obtiene exitosamente, sino False.
    '''
    def obtenAsignatura(self, cod):
>>>>>>> origin/H4-comentarios-Francisco
        try:
            codA = cod.upper()
            return self.get(pk = codA)
        except:
            return False


'''
Coordinación de postgrado. Puede tener muchas asignaturas asociadas sin
importar el departamento.
'''
>>>>>>> origin/H4-comentarios-Francisco
class Coordinacion(models.Model):
    nomCoord    = models.CharField(
        max_length = 15,
        choices = COORDS,
        primary_key = True
        )
    asignaturas = models.ManyToManyField(Asignatura, blank = True)

    class Meta:
        app_label = 'coordinaAsignaturas'
        verbose_name_plural = "Coordinaciones"

    '''
    Extrae por defecto el nombre de la coordinación.
    '''
    def __str__(self):
        return self.nomCoord

    '''
    Agrega una asignatura nueva a la base de datos a partir de sus datos
    individuales. Retorna True si la asignatura es exitosamente agregada, False
    si no.
    '''
    def agregaAsignaturaNueva(self, codAsig, codDpto, creditos, nomAsig,
        progAsig, diaHora, ciprof):
        asig = Asignatura()
        try:
            asig.codAsig  = codAsig
            asig.codDpto  = codDpto
            asig.creditos = creditos
            asig.nomAsig  = nomAsig
            asig.progAsig = progAsig
            asig.diaHora  = diaHora
            asig.prof     = Profesor.objects.get(pk = ciprof)
            asig.save()
            self.save()
            self.asignaturas.add(Asignatura.objects.get(pk = codAsig))
            return True
        except:
            return False

    '''
    Recibe el codigo de la asignatura. Devuelve True si la asignatura de codigo
    codAsig es agregada exitosamente a la lista, False si no.
    '''
    def agregaAsignaturaExistente(self, codAsig):
>>>>>>> origin/H4-comentarios-Francisco
        try:
            self.asignaturas.add(Asignatura.objects.get(pk = codAsig))
            self.save()
            return True
        except:
            return False

    '''
    Recibe codigo string. Devuelve objeto asignatura
    '''
    def obtenAsignatura(self, cod):
        try:
            codA = cod.upper()
            return self.asignaturas.get(pk = codA)
        except:
            return False

    '''
    Devuelve lista de asignaturas de la coordinación.
    '''
    def obtenAsignaturas(self):
        try:
            return list(self.asignaturas.all())
        except:
            return False

    '''
    Toma codigo string, devuelve bool.
    Elimina de la coordinacion.
    '''
    def eliminaAsignatura(self, cod):
        try:
            codA = cod.upper()
            self.asignaturas.remove(codA)
            return True
        except:
            return False

    def buscaAsignatura(self,codAsig=None,nomAsig=None,creditos=None,progAsig=None):

        try:
            por_cod = self.asignaturas.filter(codAsig__iexact=str(codAsig))
            por_nom = self.asignaturas.filter(nomAsig__icontains=str(nomAsig))
            por_cred = self.asignaturas.filter(creditos__exact=creditos)
            por_progAsig = self.asignaturas.filter(progAsig__icontains=str(progAsig))

            result = set(por_cod).union(por_nom)
            result = set(result).union(por_cred)
            result = set(result).union(por_progAsig)

            return(list(result))

        except:
            return False

'''
Coordinador de coordinación de postgrado. Tiene un usuario Django asociado
con permisología específica.
'''
class Coordinador(models.Model):
    usuario      = models.OneToOneField(Usuario, on_delete = models.CASCADE,
        primary_key = True)
    coordinacion = models.ForeignKey(Coordinacion, on_delete = models.PROTECT)

    class Meta:
        app_label = 'coordinaAsignaturas'
        verbose_name_plural = "Coordinadores"

'''
Oferta de asignaturas proveniente de una coordinación de postgrado. Puede tener muchas asignaturas. Es una oferta con trimestre y año.
'''
class Oferta(models.Model):
    coordinacion = models.ForeignKey(Coordinacion, on_delete = models.PROTECT)
    trimestre    = models.CharField(max_length = 7, choices = TRIMESTRES)
    asignaturas  = models.ManyToManyField(Asignatura)
    anio         = models.IntegerField(
        validators = [MinValueValidator(1697), MaxValueValidator(2050)]
        )

    def __str__(self):
        return ("%s %s" % (self.trimestre, self.anio))

    class Meta:
        app_label = 'coordinaAsignaturas'
        ordering = ('anio',)

'''
Inscripción de un estudiante. Consta de asignaturas, año y trimestre. Se
puede calcular la suma de créditos (carga académica) el metodo sumCreditos
'''
class Inscripcion(models.Model):
    asignaturas = models.ManyToManyField(Asignatura)
    anio        = models.IntegerField(
        validators=[MinValueValidator(1967), MaxValueValidator(2050)]
        )
    trimestre   = models.CharField(max_length = 7, choices = TRIMESTRES)

    def __str__(self):
        return ("%s %s" % (self.trimestre, self.anio))

    '''
    Funcion que permite calcular la carga académica del estudiante.
    '''
    def sumCreditos(self):
        suma = 0
        for asignatura in self.asignaturas:
            suma += asignatura.creditos
        return suma

    class Meta:
        app_label = 'coordinaAsignaturas'
        verbose_name_plural = "Inscripciones"

'''
Estudiante de postgrado. Está asociado a un usuario Django. Necesita tener
alguna inscripción para contar como estudiante.
'''
class Estudiante(models.Model):
    usuario       = models.OneToOneField(Usuario, on_delete = models.CASCADE)
    carnet        = models.CharField(max_length = 12, primary_key = True)
    inscripciones = models.ManyToManyField(Inscripcion, blank = True)
>>>>>>> origin/H4-comentarios-Francisco

    class Meta:
        app_label = 'coordinaAsignaturas'

    def __str__(self):
        nombres = "%s, %s" % (self.usuario.apellidos, self.usuario.nombres)
        return ("%s %s" % (self.carnet, nombres))

'''
Una sesion en el sistema.
'''
>>>>>>> origin/H4-comentarios-Francisco
class Sesion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.PROTECT)

    '''
    Recibe strings. Retorna Booleano
    '''
    def validaUsuario(self, usr, pwd):
        try:
            busqueda = Usuario.objects.get(pk = usr)
            hashm = hashlib.sha256()
            pswd = str.encode(pwd)
            hashm.update(pswd)
            if hashm.hexdigest() == busqueda.password:
                self.usuario = busqueda
                return True
            else:
                return False
        except:
            return False

    '''
    Retorna la coordinacion del usuario activo o False
    '''
    def obtenCoordinacion(self):
        try:
            coordinador  = Coordinador.objects.get(pk = self.usuario)
            coordinacion = coordinador.coordinacion
            return coordinacion
        except:
            return False

    class Meta:
        app_label = 'coordinaAsignaturas'

'''
Obtiene asignaturas del coordinador 'usr'
'''
>>>>>>> origin/H4-comentarios-Francisco
def obtenAsignaturas(usr):
    try:
        usuario = Usuario.objects.get(pk=usr)
        sesion = Sesion()
        sesion.usuario = usuario
        asignaturas = sesion.obtenCoordinacion().obtenAsignaturas()
        return asignaturas
    except:
        return False

'''
Busca asignaturas del coordinador 'usr' con campos flexibles
'''
def buscaAsignaturas(usr, codAsig = None, nomAsig = None, creditos = None,
    progAsig = None):
>>>>>>> origin/H4-comentarios-Francisco
    try:
        usuario        = Usuario.objects.get(pk = usr)
        sesion         = Sesion()
        sesion.usuario = usuario
        asignaturas    = sesion.obtenCoordinacion().buscaAsignatura(codAsig,
            nomAsig, creditos, progAsig)
        return asignaturas
    except:
        return False

'''
Elimina de la base de datos la asignatura de codigo 'codAsig'
'''
>>>>>>> origin/H4-comentarios-Francisco
def eliminaAsignatura(codAsig):
    try:
        return Asignatura().obtenAsignatura(codAsig).delete()
    except:
        return False


'''
Elimina la oferta 'oferta_id' de la coordinacion de 'usr'
'''
def eliminaOferta(usr, oferta_id):
>>>>>>> origin/H4-comentarios-Francisco
    try:
        usuario = Usuario.objects.get(pk = usr)
        sesion = Sesion()
        sesion.usuario = usuario
        coordinacion = sesion.obtenCoordinacion()
        oferta = Oferta.objects.get(pk = oferta_id)
        if coordinacion == oferta.coordinacion :
            oferta.delete()
            return True
        else :
            return False
    except:
        return False


'''
Elimina la asignatura 'codAsig' de la coordinacion de 'usr'
'''
def eliminaAsignaturaDeCoord(usr, codAsig):
>>>>>>> origin/H4-comentarios-Francisco
    try:
        usuario        = Usuario.objects.get(pk=usr)
        sesion         = Sesion()
        sesion.usuario = usuario
        sesion.obtenCoordinacion().asignaturas.remove(codAsig)
        return True
    except:
        return False


'''
Agrega la asignatura 'codAsig' a la coordinacion de 'usr'
'''
def agregaAsignaturaACoord(usr, codAsig):
>>>>>>> origin/H4-comentarios-Francisco
    try:
        sesion = Sesion()
        usuario = Usuario.objects.get(pk=usr)
        sesion.usuario = usuario
        sesion.obtenCoordinacion().asignaturas.add(Asignatura.objects.get(
            pk = codAsig))
    except:
        return False
    return True

'''
Retorna True o False dependiendo de si 'usr' es Estudiante o no
'''
def esEstudiante(usr):
    try:
        usuario = Usuario.objects.get(pk = usr)
        estudiante = Estudiante.objects.filter(usuario__exact = usuario)
        if estudiante.first():
            return True
        else: return False
    except:
        return False
>>>>>>> origin/H4-comentarios-Francisco
