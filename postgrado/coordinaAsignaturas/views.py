# -*- coding: utf-8 -*-


from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import *
from .forms import *

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

# Mostrar las ofertas registradas #
def verOfertas(request):
    #return HttpResponse("Estas en la vista de oferta %s" % oferta_id)
    s = Sesion()
    s.usuario = Usuario.objects.get(pk=request.session['username'])
    coord = s.obtenCoordinacion()
    ultimasOfertas = Oferta.objects.filter(coordinacion=coord)
    context = {
       'ultimasOfertas' : ultimasOfertas,
    }
    return render(request, 'coordinaAsignaturas/oferta.html', context)

# Muestra las materias registradas en la oferta #    
def detallesOferta(request, oferta_id):
    oferta_info = get_object_or_404(Oferta, pk=oferta_id)
    materiasOfertadas = oferta_info.asignaturas.all()
    return render(request, 'coordinaAsignaturas/detallesOferta.html', {'materiasOfertadas':materiasOfertadas,'oferta_info':oferta_info})

# Agrega una oferta #
def agregarOferta(request):
    form = FormCrearOferta(request.POST)
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')
    if request.method == 'POST':
        form = FormCrearOferta(request.POST)
        args = {'form' : form}
        if form.is_valid():
            form.save()
            
            return redirect('/coordinaAsignaturas/ofertas')
    else :
        args = {'form' : FormCrearAsignatura()}

    return render(request, 'coordinaAsignaturas/agregarOferta.html', {'form' : form})

# Ver las asisnaturas #
def verAsignaturas(request):
    if 'username' in request.session.keys():
        args = {'usuario' : request.session['username']}
        if request.method == 'POST' :
            try:
                return render(request, 'coordinaAsignaturas/asignaturas.html', args)
            except:
                args['asignaturas'] = []
        else :
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
            return redirect('/coordinaAsignaturas/ver')
    else :
        args = {'form' : FormCrearAsignatura()}
    return render(request, 'coordinaAsignaturas/agregarAsignatura.html', args)

#Modifica los datos de una asignatura#
def modificarAsignatura(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig=codAsig)
    
    if request.method == "POST":
        form = FormModificarAsignatura(request.POST, instance=asignatura)
        if form.is_valid():
            asignatura = form.save(commit=False)

            asignatura.save()
            return redirect('coordinaAsignaturas:detallesAsignatura', codAsig=asignatura.codAsig)
        else :
            print("Error al modificar asignatura")
    else :
        form =  FormModificarAsignatura(instance=asignatura)
    return render(request, 'coordinaAsignaturas/modificarAsignatura.html', {'form' : form})

#Elimina una asignatura de la coordinacion#
def eliminarAsignatura(request, codAsig):
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')
    try :
        eliminaAsignaturaDeCoord(request.session["username"],codAsig)
        return redirect('/coordinaAsignaturas/ver')
    except :
        return redirect('/coordinaAsignaturas/ver')

#Mustra los detalles de la asignatura#
def detallesAsignatura(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig=codAsig)
    return render(request, 'coordinaAsignaturas/detallesAsignatura.html', {'asignatura' : asignatura})

#Litar todas las asignaturas existentes##
def listaTodasAsignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'coordinaAsignaturas/listaTodasAsignaturas.html', {'asignaturas' : asignaturas})

#Agrega una asignatura a la coordinacion#
def agregarACoord(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig=codAsig)
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')
    if request.method == 'POST':
        form = FormAgregarAsignatura(request.POST, instance=asignatura)
        args = {'form' : form}
        if form.is_valid():
            #form.save()
            data = form.cleaned_data
            if (agregaAsignaturaACoord(request.session['username'],data['codAsig'])):
                args['asignaturas'] = obtenAsignaturas(request.session['username'])
                return redirect('/coordinaAsignaturas/ver')
        else :
            print("No se agrego la materia a la coordinacion")
    else :
        args = {'form' : FormAgregarAsignatura(instance=asignatura)}
    return render(request, 'coordinaAsignaturas/agregarAsignatura.html', args)