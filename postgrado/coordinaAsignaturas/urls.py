from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.urls import path

app_name = 'oferta'

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'coordinaAsignaturas/login.html'}),
	url(r'^logout/$', login, {'template_name': 'coordinaAsignaturas/logout.html'}),
	path('oferta/', views.vistaOfertas, name='oferta'),
	path('oferta/<int:oferta_id>/', views.detallesOferta, name='detalles')

]