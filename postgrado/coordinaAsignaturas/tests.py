# -*- coding: utf-8 -*-

'''
  Modulo de pruebas

  Indice de pruebas:
      1. Pruebas sobre LoginForm:
          1.1. testLoginDatosCorrectos.
          1.2. testLoginUsernameNoEsEmail.
          1.3. testLoginUsernameNoRegistrado.
          1.4. testLoginUsernameCorrectoYPasswordIncorrecta.
          1.5. testLoginUsernameVacio.
          1.6. testLoginPasswordVacio.
          1.7. testLoginUsernameYPasswordVacios.
      2. Pruebas sobre FormularioAsignatura:
          2.1.  testFormularioAsignaturaDatosCorrectos.
          2.2.  testFormularioAsignaturaCodigoMenosDeSeisCaracteres.
          2.3.  testFormularioAsignaturaCodigoMasDeSieteCaracteres.
          2.4.  testFormularioAsignaturaCodigoEmpiezaConNumero.
          2.5.  testFormularioAsignaturaCodigoTerminaConUnaLetra.
          2.6.  testFormularioAsignaturaCodigoConCaracterNoValido.
          2.7.  testFormularioAsignaturaCodigoConUnaLetra.
          2.8.  testFormularioAsignaturaCodigoConTresLetras.
          2.9.  testFormularioAsignaturaCodigoConTresDigitos.
          2.10. testFormularioAsignaturaCodigoConCincoDigitos.
          2.11. testFormularioAsignaturaCodigoRepetido.
          2.12. testFormularioAsignaturaCreditosNegativos
          2.13. testFormularioAsignaturaCreditoNoNumerico.
          2.14. testFormularioAsignaturaNombreMasDeOchentaCaracteres.
          2.15. testFormularioAsignaturaNombreConCaracteresInvalidos.
          2.16. testFormularioAsignaturaHoraInicioDespuesDeHoraFin.
          2.17. testFormularioAsignaturaFinalizaSinEmpezar.
          2.18. testFormularioAsignaturaEmpiezaYNoFinaliza.
          2.19. testFormularioAsignaturaCodigoVacio.
          2.20. testFormularioAsignaturaCreditosVacio.
          2.21. testFormularioAsignaturaNombreVacio.
          2.22. testFormularioAsignaturaProgramaVacio.
          2.23. testFormularioAsignaturaProfVacio.
          2.24. testFormularioAsignaturaVistaVacio.
          2.25. testFormularioAsignaturaVacio.
      3. Pruebas sobre FormularioOferta:
          3.1
'''
from django.test import TestCase
from coordinaAsignaturas.forms import LoginForm, FormularioAsignatura, FormularioOferta
from coordinaAsignaturas.models import Asignatura, Profesor, Usuario, Oferta
import datetime



'''
Clase de pruebas para el formulario LoginForm.
'''
class TestLoginForm(TestCase):

    # Funcion setUp agregar la instancia de Usuario que permite hacer las
    # pruebas siguientes.
    def setUp(self):
        usuario = Usuario()
        usuario.crearUsuario("coord@usb.ve", "frito")
    
    # testLoginDatosCorrectos: verifica que se retorne True al hacer login con
    # los datos correctos. Caso dentro del dominio.
    def testLoginDatosCorrectos(self):
        username = "coord@usb.ve"
        password = "frito"
        valores = { 'username': username, 'password': password }
        login = LoginForm(data = valores)
        self.assertTrue(login.is_valid())

    # testLoginUsernameNoEsEmail: verifica que se retorne False al hacer login
    # con un usuario que no es un email. Caso frontera
    def testLoginUsernameNoEsEmail(self):
        username = "username"
        password = "frito"
        valores = { 'username': username, 'password': password }
        login = LoginForm(data = valores)
        self.assertFalse(login.is_valid())

    # testLoginUsernameNoRegistrado: verifica que se retorne False al hacer
    # login con un usuario que no registrado en la base de datos. Caso frontera
    def testLoginUsernameNoRegistrado(self):
        username = "username@usb.ve"
        password = "frito"
        valores = { 'username': username, 'password': password }
        login = LoginForm(data = valores)
        self.assertFalse(login.is_valid())

    # testLoginUsernameCorrectoYPasswordIncorrecta: verifica que se retorne
    # False al hacer login con un usuario registrado y clave incorrecta. Caso
    # frontera
    def testLoginUsernameCorrectoYPasswordIncorrecta(self):
        username = "coord@usb.ve"
        password = "FRITO"
        valores = { 'username': username, 'password': password }
        login = LoginForm(data = valores)
        self.assertFalse(login.is_valid())

    # testLoginUsernameVacio: verifica que se retorne False al hacer login sin
    # ingresar un usuario registrado. Caso frontera
    def testLoginUsernameVacio(self):
        username = ""
        password = "frito"
        valores = { 'username': username, 'password': password }
        login = LoginForm(data = valores)
        self.assertFalse(login.is_valid())

    # testLoginUsernameVacio: verifica que se retorne False al hacer login sin
    # ingresar su clave. Caso frontera
    def testLoginPasswordVacio(self):
        username = "coord@usb.ve"
        password = ""
        valores = { 'username': username, 'password': password }
        login = LoginForm(data = valores)
        self.assertFalse(login.is_valid())

    # testLoginUsernameVacio: verifica que se retorne False al hacer login sin
    # ingresar ni usuario, ni clave. Caso esquina
    def testLoginUsernameYPasswordVacios(self):
        username = ""
        password = ""
        valores = { 'username': username, 'password': password }
        login = LoginForm(data = valores)
        self.assertFalse(login.is_valid())

'''
Clase de pruebas para el formulario FormularioAsignatura.
'''
class TestFormularioAsignatura(TestCase):

    # Funcion setUp agregar la instancia de Profesor que permite hacer las
    # pruebas siguientes.
    def setUp(self):
        prof = Profesor(ciProf = 12345678, nomProf = "Probador")
        prof.save()

    # testFormularioAsignaturaDatosCorrectos: verifica que se retorne True si
    # todos los datos del formulario son correctos. Caso dentro del dominio.
    def testFormularioAsignaturaDatosCorrectos(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertTrue(form.is_valid())

    # testFormularioAsignaturaCodigoMenosDeSeisCaracteres: verifica que se
    # retorne False si el codigo ingresado tiene menos de seis caracteres. Caso
    # frontera
    def testFormularioAsignaturaCodigoMenosDeSeisCaracteres(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCodigoMasDeSieteCaracteres: verifica que se
    # retorne False si el codigo ingresado tiene mas de siete caracteres. Caso
    # frontera
    def testFormularioAsignaturaCodigoMasDeSieteCaracteres(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MAA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCodigoEmpiezaConNumero: verifica que se retorne
    # False si el codigo ingresado empieza con un numero. Caso frontera
    def testFormularioAsignaturaCodigoEmpiezaConNumero(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "1A1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCodigoTerminaConUnaLetra: verifica que se retorne
    # False si el codigo ingresado termina con una letra. Caso frontera
    def testFormularioAsignaturaCodigoTerminaConUnaLetra(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA111X",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCodigoConCaracterNoValido: verifica que se
    # retorne False si el codigo ingresado tiene al menos un caracter
    # invalido. Caso frontera
    def testFormularioAsignaturaCodigoConCaracterNoValido(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA*1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCodigoConUnaLetra: verifica que se retorne False
    # si el codigo ingresado solo un caracter alfabetico. Caso frontera
    def testFormularioAsignaturaCodigoConUnaLetra(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "M1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCodigoConTresLetras: verifica que se retorne
    # False si el codigo ingresado tiene tres caracteres alfabeticos. Caso
    # frontera
    def testFormularioAsignaturaCodigoConTresLetras(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MMA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCodigoConTresDigitos: verifica que se retorne
    # False si el codigo ingresado tiene tres digitos. Caso frontera
    def testFormularioAsignaturaCodigoConTresDigitos(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCodigoConCincoDigitos: verifica que se retorne
    # False si el codigo ingresado tiene cinco digitos. Caso frontera
    def testFormularioAsignaturaCodigoConCincoDigitos(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA11115",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCodigoRepetido: verifica que se retorne False si
    # el codigo ingresado ya existe en la base de datos. Caso frontera
    def testFormularioAsignaturaCodigoRepetido(self):
        asignatura = Asignatura()
        asignatura.codAsig = "MA1111"
        asignatura.creditos = 4
        asignatura.prof = Profesor.objects.get(pk = 12345678)
        asignatura.save()
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCreditosNegativos: verifica que se retorne False
    # si los creditos ingresados son negativos. Caso frontera
    def testFormularioAsignaturaCreditosNegativos(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 20,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCreditoNoNumerico: verifica que se retorne False
    # False si los creditos ingresados no son numericos. Caso frontera
    def testFormularioAsignaturaCreditoNoNumerico(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': "cuatro",
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaNombreMasDeOchentaCaracteres: verifica que se
    # retorne False si el nombre de la asignatura supera los 80 caracteres.
    # Caso frontera
    def testFormularioAsignaturaNombreMasDeOchentaCaracteres(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I" + ("1" * 80),
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaNombreConCaracteresInvalidos: verifica que se
    # retorne False si el nombre de la asignatura tiene al menos un caracter
    # invalido. Caso frontera
    def testFormularioAsignaturaNombreConCaracteresInvalidos(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "かわいいMatemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaHoraInicioDespuesDeHoraFin: verifica que se
    # retorne False si la duracion de la asignatura es negativa. Caso frontera
    def testFormularioAsignaturaHoraInicioDespuesDeHoraFin(self):
        valores = {
            'lun': True,
            'lun_inicio': 6,
            'lun_fin': 5,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaFinalizaSinEmpezar: verifica que se retorne False
    # si se marca hora de finalizacion pero no hora de inicio. Caso frontera
    def testFormularioAsignaturaFinalizaSinEmpezar(self):
        valores = {
            'lun': True,
            # 'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaFinalizaSinEmpezar: verifica que se retorne False
    # si se marca hora de inicio pero no hora de finalizacion. Caso frontera
    def testFormularioAsignaturaEmpiezaYNoFinaliza(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            # 'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCodigoVacio: verifica que se retorne False si no
    # se ingresa el codigo de la asignatura. Caso frontera
    def testFormularioAsignaturaCodigoVacio(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            # 'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaCreditosVacio: verifica que se retorne False si
    # no se ingresan los creditos de la asignatura. Caso frontera
    def testFormularioAsignaturaCreditosVacio(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            # 'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaNombreVacio: verifica que se retorne False si no
    # se ingresa el nombre de la asignatura. Caso frontera
    def testFormularioAsignaturaNombreVacio(self):
        valores = {
            'lun': True,
            'lun_inicio': 0,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            # 'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaProgramaVacio: verifica que se retorne False si
    # no se ingresa el programa de la asignatura. Caso frontera
    def testFormularioAsignaturaProgramaVacio(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            # 'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertTrue(form.is_valid())

    # testFormularioAsignaturaProfVacio: verifica que se retorne False si no se
    # ingresa el profesor de la asignatura. Caso frontera
    def testFormularioAsignaturaProfVacio(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            # 'prof': 12345678,
            'codDpto': "MA",
            'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

    # testFormularioAsignaturaVistaVacio: verifica que se retorne False si no
    # se ingresa el campo 'vista' de la asignatura. Caso frontera
    def testFormularioAsignaturaVistaVacio(self):
        valores = {
            'lun': True,
            'lun_inicio': 5,
            'lun_fin': 6,
            'mar': False,
            'mar_inicio': 1,
            'mar_fin': 1,
            'mie': True,
            'mie_inicio': 5,
            'mie_fin': 6,
            'jue': False,
            'jue_inicio': 1,
            'jue_fin': 1,
            'vie': True,
            'vie_inicio': 5,
            'vie_fin': 6,
            'codAsig': "MA1111",
            'creditos': 4,
            'nomAsig': "Matemáticas I",
            'progAsig': "PROG-106",
            'prof': 12345678,
            'codDpto': "MA",
            # 'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertTrue(form.is_valid())

    # testFormularioAsignaturVacio: verifica que se retorne False si no se
    # ingresa ningun campo al formulario. Caso esquina
    def testFormularioAsignaturaVacio(self):
        valores = {
            # 'lun': True,
            # 'lun_inicio': 5,
            # 'lun_fin': 6,
            # 'mar': False,
            # 'mar_inicio': 1,
            # 'mar_fin': 1,
            # 'mie': True,
            # 'mie_inicio': 5,
            # 'mie_fin': 6,
            # 'jue': False,
            # 'jue_inicio': 1,
            # 'jue_fin': 1,
            # 'vie': True,
            # 'vie_inicio': 5,
            # 'vie_fin': 6,
            # 'codAsig': "MA1111",
            # 'creditos': 4,
            # 'nomAsig': "Matemáticas I",
            # 'progAsig': "PROG-106",
            # 'prof': 12345678,
            # 'codDpto': "MA",
            # 'vista': False
        }
        form = FormularioAsignatura(data = valores)
        self.assertFalse(form.is_valid())

'''
Clase de pruebas para el formulario FormularioOferta
'''
class TestFormularioOferta(TestCase):

    # Funcion setUp agregar la instancia de Profesor que permite hacer las
    # pruebas siguientes.
    def setUp(self):
        usuario = Usuario()
        usuario.crearUsuario("coord@usb.ve", "frito")
        fecha = datetime.datetime.now()


    # testOfertaDatosCorrectos: verifica que se retorne True al crear una
    # oferta con datos correctos. Caso dentro del dominio

    def testOfertaDatosCorrectos(self):
        trimestre = 'Ene-Mar'
        anio      = '2019'
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())

    # testOfertaDatosCorrectos: verifica que se retorne True al crear una
    # oferta con datos correctos. Caso dentro del dominio

    def testOfertaDatosCorrectos(self):
        trimestre = 'Ene-Mar'
        anio      = '2019'
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())

    # testOfertaAnioMinimo: verifica que se retorne True al crear una
    # oferta con el año de apertura de la Universidad. Caso dentro del dominio

    def testOfertaAnioMinimo(self):
        trimestre = 'Sept-Dic'
        anio      = '1970'
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())

    # testOfertaAnioAnterior: verifica que se retorne False al crear una
    # oferta con un año anterior al de apertura de la Universidad. Caso frontera

    def testOfertaAnioAnterior(self):
        trimestre = 'Sept-Dic'
        anio      = '1969'
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertFalse(oferta.is_valid())

    # testOfertaAnioMinimoTrimestrePrimero: verifica que se retorne True al crear una
    # oferta con un año igual al de apertura de la Universidad en el primer
    # trimestre (Primera clase magistral dada en enero de 1970). Caso Esquina

    def testOfertaAnioMinimoTrimestrePrimero(self):
        trimestre = 'Ene-Mar'
        anio      = '1970'
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())

    # testOfertaAnioMinimoTrimestreUltimo: verifica que se retorne True al crear una
    # oferta con un año igual al de apertura de la Universidad en el ultimo
    # trimestre. Caso Esquina

    def testOfertaAnioMinimoTrimestreUltimo(self):
        trimestre = 'Sept-Dic'
        anio      = '1966'
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())

    # testOfertaAnioActualTrimestrePrimero: verifica que se retorne True al crear una
    # oferta con un año actual y en el primer trimestre. Caso Esquina

    def testOfertaAnioActualTrimestrePrimero(self):
        trimestre = 'Ene-Mar'
        anio      = fecha.year()
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())

    # testOfertaAnioActualTrimestreSegundo: verifica que se retorne True al crear una
    # oferta con un año actual y en el segundo trimestre. Caso Malicia

    def testOfertaAnioActualTrimestreSegundo(self):
        trimestre = 'Abr-Jul'
        anio      = fecha.year()
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())

    # testOfertaAnioActualTrimestreUltimo: verifica que se retorne True al crear una
    # oferta con un año actual y en el ultimo trimestre. Caso Esquina

    def testOfertaAnioActualTrimestreUltimo(self):
        trimestre = 'Sept-Dic'
        anio      = fecha.year
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())

    # testOfertaAnioLejanoTrimestrePrimero: verifica que se retorne True al crear una
    # oferta con un año lejano y en el primer trimestre. Caso Esquina

    def testOfertaAnioLejanoTrimestrePrimero(self):
        trimestre = 'Ene-Mar'
        anio      = '2050'
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())


    # testOfertaAnioLejanoTrimestreSegundo: verifica que se retorne True al crear una
    # oferta con un año lejano y en el segundo trimestre. Caso Malicia

    def testOfertaAnioLejanoTrimestreSegundo(self):
        trimestre = 'Abr-Jul'
        anio      = '2050'
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())

    # testOfertaAnioLejanoTrimestreUltimo: verifica que se retorne True al crear una
    # oferta con un año lejano y en el segundo trimestre. Caso Malicia

    def testOfertaAnioLejanoTrimestreUltimo(self):
        trimestre = 'Sept-Dic'
        anio      = '2050'
        valores   = {'trimestre' : trimestre, 'anio': anio}
        oferta    = FormularioOferta(data = valores)
        self.assertTrue(oferta.is_valid())        