# -*- coding: utf-8 -*-


from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.urls import path

app_name = 'coordinaAsignaturas'
urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', views.home),
	url(r'^logout/$', login, {'template_name': 'coordinaAsignaturas/logout.html'}),
	url(r'^ver/$', views.vistaAsignaturas, name='verAsignaturas'),
	url(r'^eliminar/(?P<codAsig>[-\w]+)', views.eliminarAsignatura, name="eliminarAsignatura"),
	#url(r'^agregar/', views.agregarAsignatura),
	#url(r'^editar/', views.editarAsignatura),
	path('modificar/(?P<codAsig>[-\w]+)', views.modificarAsignatura, name='modificarAsignatura'),
	path('agregar/', views.agregarAsignatura, name='agregarAsignatura'),
	path('detalles/', views.detallesAsignatura, name='detallesAsignatura'),
	path('principal/', views.principal, name='principal'),
	path('<int:oferta_id>/', views.vistaOfertas, name='oferta')
]