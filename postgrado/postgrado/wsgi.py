# -*- coding: utf-8 -*-

'''
Universidad Simón Bolívar
Ingeniería de Software I CI-3715
Sistema de gestión de postgrados de la USB

Coniguración WSGI

Este módulo no se ha modificado

'''


"""
WSGI config for postgrado project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "postgrado.settings")

application = get_wsgi_application()
