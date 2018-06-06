# -*- coding: utf-8 -*-


from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from coordinaAsignaturas.models import *
from coordinaAsignaturas.forms import *
# Create your views here.
def home(request):
    if request.method == "POST" :
        form = LoginForm(request.POST)
        args = {'form': form}
        if form.is_valid() :
            sesion = Sesion()
            if sesion.validaUsuario(form['username'].value(),form['password'].value()):
                args['sesion'] = sesion
                context = { 'asignaturas' : args['sesion'].obtenCoordinacion().obtenAsignaturas()}
                return render(request,'coordinaAsignaturas/ver_asignaturas.html',context)
                
                


    else :
        args = {'form': LoginForm()}
    return render(request, 'coordinaAsignaturas/login.html', args)

# Pagina principal #
def principal(request):
    return render(request, 'coordinaAsignaturas/initIndex.html', {})

# Vista de las ofertas #
def vistaOfertas(request, oferta_id):
    #return HttpResponse("Estas en la vista de oferta %s" % oferta_id)
    #ultimasOfertas = Oferta.objects
    #template = loader.get_template('coordinaAsignaturas/oferta.html')
    #context = {
    #   'ultimasOfertas' : ultimasOfertas,
    #}
    #return render(request, 'coordinaAsignaturas/oferta.html', context)
    pass

# Ver las asisnaturas #
def vistaAsignaturas(request):
    if request.method == 'POST' :
        try:
            coordinacion = args['']
            args = {'asignaturas' : Asignatura.objects(coordinacion.obtenAsignaturas())}
        except:
            args = {'asignaturas' : []}
    else :
        args = {'asignaturas' : Asignatura.objects.all()}
    return render(request, 'coordinaAsignaturas/ver_asignaturas.html', args)

# Agregar una asignatura #
def agregarAsignatura(request):
    if request.method == 'POST':
      form = FormularioAsignatura(request.POST)
      args = {'form' : form}
      if form.is_valid():
          form.save()
    else :
      args = {'form' : FormularioAsignatura()}
    return render(request, 'coordinaAsignaturas/agregar_asignatura.html', args)

# Editar una asignatura #
def editarAsignatura(request):
    return render(request, 'coordinaAsignaturas/editAsignatura.html', {})

# Detalles de una oferta #
def detallesAsignatura(request):
    return render(request, 'coordinaAsignaturas/detailAsignatura.html', {})