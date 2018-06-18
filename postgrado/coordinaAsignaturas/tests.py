from django.test import TestCase
from coordinaAsignaturas.models import *
from coordinaAsignaturas.forms import *

class TestUsuario(TestCase):
    def testUsuarioNuevo(self):
        usuario = Usuario()
        username = "usuario"
        clave = "1234"
        dic ={'username':'usuario', 'password':'1234'}
        form = LoginForm(dic)
        self.assertFalse(form.is_valid())