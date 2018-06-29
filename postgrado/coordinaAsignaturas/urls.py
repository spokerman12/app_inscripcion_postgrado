# -*- coding: utf-8 -*-
# Variables:
#	 app_name = Nombre de la aplicacion.
#	 urlpatterns: lista de las URL de la aplicacion.

from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout

app_name = 'coordinaAsignaturas'
urlpatterns = [
	# URL para LOGIN.
	url(r'^login/$', views.home, name = 'login'),
	# URL principal DESPUES de hacer login.
	url(r'^principal/$', views.principal, name = 'principal'),
	# URL para ver las asignaturas disponibles.
	url(r'^ver/$', views.verAsignaturas, name = 'verAsignaturas'),
	# URL para agregar una nueva asignatura.
	url(r'^agregar/$', views.agregarAsignatura, name = 'agregarAsignatura'),
	# URL para modificar una asignatura dado su codigo.
	url(
		r'^modificar/(?P<codAsig>.+)/$',
		views.modificarAsignatura,
		name = 'modificarAsignatura'
		),
	# URL para eliminar una asignatura dado su codigo.
	url(
		r'^eliminar/(?P<codAsig>[-\w]+)',
		views.eliminarAsignatura,
		name = 'eliminarAsignatura'
		),
	# URL para ver los detalles de una asignatura dado su codigo.
	url(
		r'^detalles/(?P<codAsig>.+)/$',
		views.detallesAsignatura,
		name = 'detallesAsignatura'
		),
	# URL para ver la lista de ofertas de asignaturas de una coordinacion.
	url(r'^ofertas/$', views.verOfertas, name = 'oferta'),
	# URL para ver detalles de una oferta de asignaturas de una coordinacion.
	url(
		r'^ofertas/(?P<oferta_id>[0-9]+)/$',
		views.detallesOferta,
		name = 'detallesOferta'
		),
	# URL para agregar una nueva oferta de asignaturas de una coordinacion.
	url(r'^agregarOferta/$', views.agregarOferta, name = 'agregarOferta'),
	# URL para modificar una oferta de asignaturas de una coordinacion.
	url(
		r'^modificarOferta/(?P<oferta_id>[0-9]+)/$',
		views.modificarOferta,
		name = 'modificarOferta'
		),
	# URL para eliminar una oferta de asignaturas de una coordinacion.
	url(
		r'^eliminarOferta/(?P<oferta_id>[0-9]+)',
		views.eliminarOferta,
		name = 'eliminarOferta'
		),
	# URL para listar todas las asignaturas existentes en la base de datos.
	url(
		r'^listaAsignaturas/$',
		views.listaTodasAsignaturas,
		name = 'listaTodasAsignaturas'
		),
	# URL para 
	url(
		r'^agregarACoord/(?P<codAsig>.+)/$',
		views.agregarACoord,
		name = 'agregarACoord'
		),
	#url(r'^logout/$', login, {'template_name': 'coordinaAsignaturas/logout.html'}),
]