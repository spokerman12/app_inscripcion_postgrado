# -*- coding: utf-8 -*-


from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout


app_name = 'coordinaAsignaturas'
urlpatterns = [
	url(r'^login/$', views.home, name='login'),
	url(r'^principal$', views.principal, name='principal'),
	url(r'^principal$', views.principal, name='principal'),
	url(r'^ver/$', views.verAsignaturas, name='verAsignaturas'),
	url(r'^agregar/$', views.agregarAsignatura, name='agregarAsignatura'),
	url(r'^modificar/(?P<codAsig>.+)/$', views.modificarAsignatura, name='modificarAsignatura'),
	url(r'^eliminar/(?P<codAsig>[-\w]+)', views.eliminarAsignatura, name="eliminarAsignatura"),
	url(r'^detalles/(?P<codAsig>.+)/$', views.detallesAsignatura, name='detallesAsignatura'),
	url(r'^ofertas/$', views.verOfertas, name='oferta'),
	url(r'^ofertas/(?P<oferta_id>[0-9]+)/$', views.detallesOferta, name='detallesOferta'),
	url(r'^agregarOferta/$', views.agregarOferta, name='agregarOferta'),
	url(r'^modificarOferta/(?P<oferta_id>[0-9]+)/$', views.modificarOferta, name='modificarOferta'),
	url(r'^eliminarOferta/(?P<oferta_id>[0-9]+)', views.eliminarOferta, name="eliminarOferta"),
	url(r'^listaAsignaturas/$', views.listaTodasAsignaturas, name="listaTodasAsignaturas"),
	url(r'^agregarACoord/(?P<codAsig>.+)/$', views.agregarACoord, name="agregarACoord"),
	#url(r'^logout/$', login, {'template_name': 'coordinaAsignaturas/logout.html'}),
]