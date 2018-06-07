
class Usuario(models.Model):
    username    = models.EmailField(max_length=30, primary_key=True)
    password    = models.CharField(max_length=64, null=False)
    nombres     = models.CharField(max_length=80)
    apellidos   = models.CharField(max_length=80)

    # Recibe strings. Devuelve Bool
    def crearUsuario(self,usr,pwd):

class Profesor(models.Model):
    ciProf      = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(99999999)], primary_key=True)
    nomProf     = models.CharField(max_length=80)

class Asignatura(models.Model):
    codAsig     = models.CharField(max_length=7, primary_key=True)
    codDpto     = models.CharField(max_length=6, choices = DPTOS)
    creditos    = models.IntegerField(choices = ((0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),
                                                (7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15)))
    nomAsig     = models.CharField(max_length=80)
    progAsig    = models.CharField(max_length=20)
    diaHora     = models.CharField(max_length=60)
    prof        = models.ForeignKey(Profesor, on_delete=models.PROTECT)

class Coordinacion(models.Model):
    nomCoord    = models.CharField(max_length=15, choices = COORDS, primary_key=True)
    asignaturas = models.ManyToManyField(Asignatura, blank = True)


    # Recibe codigo string. Devuelve objeto asignatura
    def obtenAsignatura(self,cod):

    # Devuelve lista de asignaturas
    def obtenAsignaturas(self):

    # ciprof y creditos son int. Los demas string.
    # Devuelve bool
    def agregaAsignaturaNueva(self,codAsig,codDpto,creditos,nomAsig,progAsig,diaHora,ciprof):

    # Recibe el codigo de la asignatura. Devuelve bool
    def agregaAsignaturaExistente(self,codAsig):

class Coordinador(models.Model):
    usuario          = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    coordinacion   = models.ForeignKey(Coordinacion, on_delete=models.PROTECT)

class Oferta(models.Model):
    coordinacion    = models.ForeignKey(Coordinacion, on_delete=models.PROTECT)
    trimestre   = models.CharField(max_length=7, choices = TRIMESTRES)
    asignaturas = models.ManyToManyField(Asignatura)
    anio        = models.IntegerField(validators=[MinValueValidator(fecha.year),MaxValueValidator(2050)])

class Inscripcion(models.Model):
    asignaturas = models.ManyToManyField(Asignatura)
    anio        = models.IntegerField(validators=[MinValueValidator(fecha.year),MaxValueValidator(2050)])
    trimestre   = models.CharField(max_length=7, choices=TRIMESTRES)

    # Devuelve la suma de creditos de las asignaturas inscritas
    def sumCreditos(self):

class Estudiante(models.Model):
    usuario         = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    carnet          = models.CharField(max_length=12, primary_key=True)
    inscripciones   = models.ManyToManyField(Inscripcion)

class Sesion(models.Model):
    usuario     = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    # Recibe strings. Retorna Booleano
    def validaUsuario(self,usr,pwd):

    # Retorna la coordinacion del usuario activo o False
    def obtenCoordinacion(self):
