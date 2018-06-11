# -*- coding: utf-8 -*-


from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import *
from .forms import *
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

def principal(request):
    asignaturas = Asignatura.objects.all()
    context = {'asignaturas' : asignaturas}
    return render(request, 'coordinaAsignaturas/initIndex.html', context)

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
    if 'username' in request.session.keys():
        args = {'usuario' : request.session['username']}
        if request.method == 'POST' :
            try:
                return render(request, 'coordinaAsignaturas/asignaturas.html', args)
            except:
                args['asignaturas'] = []
        else :
            #args['asignaturas'] = coordinacion.obtenAsignaturas()
            args['asignaturas'] = obtenAsignaturas(request.session['username'])
            if not args['asignaturas'] :
                args['asignaturas'] = []
        return render(request, 'coordinaAsignaturas/asignaturas.html', args)
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
            data = form.cleaned_data
            agregaAsignaturaACoord(request.session['username'],data['codAsig'])
            args['asignaturas'] = obtenAsignaturas(request.session['username'])
            return render(request, 'coordinaAsignaturas/asignaturas.html', args)
    else :
        args = {'form' : FormCrearAsignatura()}
    return render(request, 'coordinaAsignaturas/agregarAsignatura.html', args)

def editarAsignatura(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig=codAsig)
    
    #post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = FormModificarAsignatura(request.POST, instance=asignatura)
        if form.is_valid():
            asignatura = form.save(commit=False)
            #asignatura. = ''
            asignatura.save()
            return redirect('coordinaAsignaturas:detallesAsignatura', codAsig=asignatura.codAsig)
    else :
        form =  FormModificarAsignatura(instance=asignatura)
    return render(request, 'coordinaAsignaturas/editAsignatura.html', {'form' : form})

def detallesAsignatura(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig=codAsig)
    return render(request, 'coordinaAsignaturas/detailAsignatura.html', {'asignatura' : asignatura})