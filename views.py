# -*- coding: utf-8 -*-


from django.shortcuts import render, HttpResponse
from django.template import loader
from coordinaAsignaturas.models import *
from coordinaAsignaturas.forms import *
# Create your views here.
def home(request):

	numbers = [1,2,3,4,5]
	name = 'Max Power'

	args = {'myName': name, 'numbers': numbers}
	return render(request, 'coordinaAsignaturas/login.html', args)

def vistaOfertas(request, oferta_id):
	#return HttpResponse("Estas en la vista de oferta %s" % oferta_id)
	#ultimasOfertas = Oferta.objects
	#template = loader.get_template('coordinaAsignaturas/oferta.html')
	#context = {
	#	'ultimasOfertas' : ultimasOfertas,
	#}
	#return render(request, 'coordinaAsignaturas/oferta.html', context)
	pass

# Ver las asisnaturas #
def vistaAsignaturas(request):
	args = {'asignaturas' : Asignatura.objects.all()}
	return render(request, 'coordinaAsignaturas/asignaturas.html', args)

# Agregar una asignatura #
def agregarAsignatura(request):
	#if request.method == 'POST':
	#	form = FormularioAsignatura(request.POST)
	#	args = {'form' : form}
	#	if form.is_valid():
	#		form.save()
	#else :
	#	args = {'form' : FormularioAsignatura()}
	return render(request, 'coordinaAsignaturas/addAsignatura.html', {})

def editarAsignatura(request):
	return render(request, 'coordinaAsignaturas/editAsignatura.html', {})

def detallesAsignatura(request):
	return render(request, 'coordinaAsignaturas/detailAsignatura.html', {})