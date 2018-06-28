# -*- coding: utf-8 -*-

'''
Universidad Simón Bolívar
Ingeniería de Software I CI-3715
Sistema de gestión de postgrados de la USB

Vistas de postgrado

Desarrollado por Equipo Null Pointer Exception

'''


from django.shortcuts import redirect


'''
login_redirect: Redirige al usuario a la pantalla de login

'''
def login_redirect(request):
	return redirect('/coordinaAsignaturas/login')