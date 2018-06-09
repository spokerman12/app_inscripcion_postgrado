# -*- coding: utf-8 -*-

from django.shortcuts import redirect

def login_redirect(request):
	return redirect('/coordinaAsignaturas/login')