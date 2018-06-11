# -*- coding: utf-8 -*-


from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout


app_name = 'coordinaAsignaturas'
urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', views.home),
	#url(r'^logout/$', login, {'template_name': 'coordinaAsignaturas/logout.html'}),
	url(r'^principal/$', views.principal, name='principal'),
	url(r'^ver/$', views.vistaAsignaturas, name='verAsignatura'),
	url(r'^editar/(?P<codAsig>.+)/$', views.editarAsignatura, name='editarAsignatura'),
	url(r'^agregar/$', views.agregarAsignatura, name='agregarAsignatura'),
	url(r'^detalles/(?P<codAsig>.+)/$', views.detallesAsignatura, name='detallesAsignatura'),
	url(r'^<int:oferta_id>/$', views.vistaOfertas, name='oferta')
]