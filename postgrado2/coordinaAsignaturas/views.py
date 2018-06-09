# -*- coding: utf-8 -*-


from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template import loader
from .models import *
from .forms import *
# Create your views here.
def home(request):

	numbers = [1,2,3,4,5]
	name = 'Max Power'

	args = {'myName': name, 'numbers': numbers}
	return render(request, 'coordinaAsignaturas/login.html', args)

def principal(request):
	asignaturas = Asignatura.objects.all()
	context = {'asignaturas' : asignaturas}
	return render(request, 'coordinaAsignaturas/initIndex.html', context)

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
	asignaturas = Asignatura.objects.all()
	args = {'asignaturas' : asignaturas}
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

def editarAsignatura(request, codAsig):
	asignatura = get_object_or_404(Asignatura, codAsig=codAsig)
	
	#post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = FormModificarAsignatura(request.POST, instance=asignatura)
		if form.is_valid():
			asignatura = form.save(commit=False)
			#asignatura. = ''
			asignatura.save()
			return redirect('coordinaAsignaturas:detallesAsignatura', codAsig=asignatura.codAsig)
	else :
		form =  FormModificarAsignatura(instance=asignatura)
	return render(request, 'coordinaAsignaturas/editAsignatura.html', {'form' : form})

def detallesAsignatura(request, codAsig):
	asignatura = get_object_or_404(Asignatura, codAsig=codAsig)
	return render(request, 'coordinaAsignaturas/detailAsignatura.html', {'asignatura' : asignatura})