from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from coordinaAsignaturas.models import *
from django.http import Http404
# Create your views here.
def home(request):

	numbers = [1,2,3,4,5]
	name = 'Max Power'

	args = {'myName': name, 'numbers': numbers}
	return render(request, 'coordinaAsignaturas/login.html', args)

def vistaOfertas(request):
	#return HttpResponse("Estas en la vista de oferta %s" % oferta_id)
	ultimasOfertas = Oferta.objects.order_by('id')
	template = loader.get_template('coordinaAsignaturas/oferta.html')
	context = {
		'ultimasOfertas' : ultimasOfertas,
	}
	return render(request, 'coordinaAsignaturas/oferta.html', context)

def detallesOferta(request, oferta_id):
	oferta = get_object_or_404(Oferta, pk=oferta_id)
	return render(request, 'coordinaAsignaturas/detallesOferta.html', {'oferta' : oferta})