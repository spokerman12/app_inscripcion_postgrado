# -*- coding: utf-8 -*-


from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.urls import path

app_name = 'coordinaAsignaturas'
urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'coordinaAsignaturas/login.html'}),
	url(r'^logout/$', login, {'template_name': 'coordinaAsignaturas/logout.html'}),
	url(r'^ver/$', views.vistaAsignaturas, name='verAsignatura'),
	#url(r'^agregar/', views.agregarAsignatura),
	#url(r'^editar/', views.editarAsignatura),
	path('editar/', views.editarAsignatura, name='editarAsignatura'),
	path('agregar/', views.agregarAsignatura, name='agregarAsignatura'),
	path('detalles/', views.detallesAsignatura, name='detallesAsignatura'),
	path('<int:oferta_id>/', views.vistaOfertas, name='oferta')
]