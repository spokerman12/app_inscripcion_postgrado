#!/usr/bin/python3
"""
Titulo: pruebas.py

Descripcion: Suite de pruebas para PyUnit

Equipo: Null Pointer Exception

Fecha: 29/05/2018.
"""

import unittest

from coordinaAsignaturas.models import *

class FuncionTestCase(unittest.TestCase):
    
    # 1. Comprueba que existe la clase seguridad.
    # Tipo: Arbitrario.
    # Conduce: Daniel
    def test_SeguridadExists(self) -> 'void':
        prueba = Seguridad()


if __name__ == "__main__":
    unittest.main()