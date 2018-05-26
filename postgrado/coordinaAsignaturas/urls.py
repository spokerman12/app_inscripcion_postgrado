from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'coordinaAsignaturas/login.html'}),
	url(r'^logout/$', login, {'template_name': 'coordinaAsignaturas/logout.html'})

]