# -*- coding: utf-8 -*-
'''

Universidad Simón Bolívar
Ingeniería de Software I CI-3715
Sistema de gestión de postgrados de la USB
Url's para la aplicación coordinaAsignaturas

Desarrollado por Equipo Null Pointer Exception

 Variables:
	 app_name = Nombre de la aplicación.
	 urlpatterns: lista de las URL de la aplicación.
'''

from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout


app_name = 'coordinaAsignaturas'
urlpatterns = [

	# URL que direcciona a la página del LOGIN.
	url(r'^login/$', views.home, name = 'login'),

	# URL que direcciona a la página principal DESPUES de hacer login.
	url(r'^principal/$', views.principal, name = 'principal'),

	# URL que direcciona a la página para ver las asignaturas disponibles.
	url(r'^ver/$', views.verAsignaturas, name = 'verAsignaturas'),

	# URL que direcciona a la página para agregar una nueva asignatura.
	url(r'^agregar/$', views.agregarAsignatura, name = 'agregarAsignatura'),

	# URL que direcciona a la página para modificar una asignatura
	url(r'^modificar/(?P<codAsig>.+)/$',
		views.modificarAsignatura,
		name = 'modificarAsignatura'
		),

	# URL que direcciona a la página para eliminar una asignatura
	url(r'^eliminar/(?P<codAsig>[-\w]+)',
		views.eliminarAsignatura,
		name = 'eliminarAsignatura'
		),

	# URL que direcciona a la página para ver los detalles de una asignatura
	url(
		r'^detalles/(?P<codAsig>.+)/$',
		views.detallesAsignatura,
		name = 'detallesAsignatura'
		),

	# URL que direcciona a la página para ver la lista de ofertas de
	# asignaturas de la coordinación.
	url(r'^ofertas/$', views.verOfertas, name = 'oferta'),

	# URL que direcciona a la página para ver detalles de una oferta de
	# asignaturas de una coordinación.
	url(
		r'^ofertas/(?P<oferta_id>[0-9]+)/$',
		views.detallesOferta,
		name = 'detallesOferta'
		),

	# URL que direcciona a la página para agregar una nueva oferta de
	# asignaturas de una coordinación.
	url(r'^agregarOferta/$', views.agregarOferta, name = 'agregarOferta'),

	# URL que direcciona a la página para modificar una oferta de
	# asignaturas de una coordinación.
	url(
		r'^modificarOferta/(?P<oferta_id>[0-9]+)/$',
		views.modificarOferta,
		name = 'modificarOferta'
		),

	# URL que direcciona a la página para eliminar una oferta de
	# asignaturas de una coordinación.
	url(
		r'^eliminarOferta/(?P<oferta_id>[0-9]+)',
		views.eliminarOferta,
		name = 'eliminarOferta'
		),

	# URL que direcciona a la página para listar todas las asignaturas
	# existentes en la base de datos.
	url(
		r'^listaAsignaturas/$',
		views.listaTodasAsignaturas,
		name = 'listaTodasAsignaturas'
		),

	# URL que direcciona a la página para agregar una asignatura existente en la
	# base de datos a la coordinación
	url(
		r'^agregarACoord/(?P<codAsig>.+)/$',
		views.agregarACoord,
		name = 'agregarACoord'
		),
]