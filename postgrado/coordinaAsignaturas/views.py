from django.shortcuts import render, HttpResponse
from django.template import loader
from coordinaAsignaturas.models import *
# Create your views here.
def home(request):

	numbers = [1,2,3,4,5]
	name = 'Max Power'

	args = {'myName': name, 'numbers': numbers}
	return render(request, 'coordinaAsignaturas/login.html', args)

def vistaOfertas(request, oferta_id):
	return HttpResponse("Estas en la vista de oferta %s" % oferta_id)
	#ultimasOfertas = Oferta.objects
	#template = loader.get_template('coordinaAsignaturas/oferta.html')
	#context = {
	#	'ultimasOfertas' : ultimasOfertas,
	#}
	#return render(request, 'coordinaAsignaturas/oferta.html', context)