# -*- coding: utf-8 -*-

'''
Universidad Simón Bolívar
Ingeniería de Software I CI-3715
Sistema de gestión de postgrados de la USB

Vistas de coordinaAsignaturas

Desarrollado por Equipo Null Pointer Exception

'''

from django.conf.urls import url, include
from django.contrib import admin
from postgrado import views
from django.conf import settings
from django.conf.urls.static import static


'''
urlpatterns: Patrones de URL para postgrado

Nótese que views.login_redirect recibe una expresión regular vacía


'''

urlpatterns = [
	url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^coordinaAsignaturas/', include('coordinaAsignaturas.urls')),
    #url(r'login/$', login, {'template_name': 'coordinaAsignaturas/login.html'})
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
