# -*- coding: utf-8 -*-


from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.template import loader
from coordinaAsignaturas.models import *
from coordinaAsignaturas.forms import *
# Create your views here.
def home(request):
    if request.method == "POST" :
        form = LoginForm(request.POST)
        args = {'form': form}
        if form.is_valid() :
            request.session['username'] = form.cleaned_data['username']
            return redirect('/coordinaAsignaturas/ver')
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

# Ver las asignaturas #
def vistaAsignaturas(request):
    if 'username' in request.session.keys():
        args = {'usuario' : request.session['username']}
        if request.method == 'POST' :
            try:
                args['asignaturas'] = buscaAsignaturas(request.session['username'],codAsig=request.POST['search'],nomAsig=request.POST['search'])
            except:
                args['asignaturas'] = []
        else :
            #args['asignaturas'] = coordinacion.obtenAsignaturas()
            args['asignaturas'] = obtenAsignaturas(request.session['username'])
            if not args['asignaturas'] :
                args['asignaturas'] = []
        return render(request, 'coordinaAsignaturas/ver_asignaturas.html', args)
    else :
        return redirect('/coordinaAsignaturas/login')

# Agregar una asignatura #
def agregarAsignatura(request):
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')
    if request.method == 'POST':
      form = FormCrearAsignatura(request.POST)
      args = {'form' : form}
      if form.is_valid():
          form.save()
          return redirect('/coordinaAsignaturas/ver')
    else :
      args = {'form' : FormCrearAsignatura()}
    return render(request, 'coordinaAsignaturas/agregar_asignatura.html', args)

def modificarAsignatura(request, codAsig):
    asig = get_object_or_404(Asignatura, codAsig=codAsig)
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')
    if request.method == "POST":
        form = FormCrearAsignatura(request.POST, instance=asig)
        args = {'form' : form}
        if form.is_valid():
            aux = form.save(commit=False)
            #Aqui guardar la asignatura para la coordinacion#
            aux.save()
            return redirect('/coordinaAsignaturas/ver')
    else :
        form = FormCrearAsignatura(instance=codAsig)
        #return redirect('/coordinaAsignaturas/login')
    return render(request, 'coordinaAsignaturas/agregar_asignatura.html', args)

def eliminarAsignatura(request, codAsig):
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')
    try :
        asig = Asignatura.objects.get(pk=codAsig)
        asig.delete()
        return redirect('/coordinaAsignaturas/ver')
    except :
        return redirect('/coordinaAsignaturas/ver')

# Editar una asignatura #
def editarAsignatura(request):
    return render(request, 'coordinaAsignaturas/editAsignatura.html', {})

# Detalles de una oferta #
def detallesAsignatura(request):
    return render(request, 'coordinaAsignaturas/detailAsignatura.html', {})