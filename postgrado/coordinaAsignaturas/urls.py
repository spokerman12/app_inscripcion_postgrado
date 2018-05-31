from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.urls import path

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'coordinaAsignaturas/login.html'}),
	url(r'^logout/$', login, {'template_name': 'coordinaAsignaturas/logout.html'}),
	url(r'^ver/', views.vistaAsignaturas),
	url(r'^agregar/', views.agregarAsignatura),
	path('<int:oferta_id>/', views.vistaOfertas, name='oferta')
]