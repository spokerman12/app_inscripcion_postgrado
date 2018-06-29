# -*- coding: utf-8 -*-

'''

Universidad Simón Bolívar
Ingeniería de Software I CI-3715
Sistema de gestión de postgrados de la USB
Vistas para la aplicación coordinaAsignaturas

Desarrollado por Equipo Null Pointer Exception

 Indice de vistas:
      1.  home.
      2.  principal.
      3.  verAsignaturas.
      4.  agregarAsignatura.
      5.  modificarAsignatura.
      6.  eliminarAsignatura.
      7.  detallesAsignatura.
      8.  listaTodasAsignaturas.
      9.  agregarACoord.
      10. verOfertas.
      11. detallesOferta.
      12. agregarOferta.
      13. modificarOferta.
      14. eliminarOferta.

'''

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from coordinaAsignaturas.forms import *
from coordinaAsignaturas.models import *


'''#############################################################################

                            Vistas principales

'''#############################################################################


'''
1.  home
        Vista que representa la página de inicio de sesión
'''
def home(request):

    if request.method == "POST":

        # Si se recibe información del método POST, recibimos el formulario
        form = LoginForm(request.POST)
        args = {'form': form}

        # Se verifica si el form es válido. Ver form.is_valid en forms.py
        if form.is_valid():
            request.session['username'] = form.cleaned_data['username']
            if esEstudiante(request.session['username']):
                return render(request, 'coordinaAsignaturas/login.html', args)
            else:
                return redirect('/coordinaAsignaturas/principal')
    else:

        # Primero se reproduce el formulario
        args = {'form': LoginForm()}
    return render(request, 'coordinaAsignaturas/login.html', args)


'''
2.  principal
        Vista que representa la página principal para el coordinador
'''
def principal(request):

    # Solicitamos todas las asignaturas a la base de datos
    asignaturas = Asignatura.objects.all()
    context = {'asignaturas': asignaturas}
    return render(request, 'coordinaAsignaturas/initIndex.html', context)


'''#############################################################################

                        Vistas sobre las asignaturas

'''#############################################################################

'''
3.  verAsignaturas
        Vista que muestra todas las asignaturas de la coordinación
'''
def verAsignaturas(request):

    # Redirección al login si no hay sesión
    if 'username' in request.session.keys():
        args = { 'usuario' : request.session['username'] }

        # Se pasa un request con las asignaturas en args
        if request.method == 'POST':
            try:
                return render(request, 'coordinaAsignaturas/asignaturas.html',
                              args)
            except:
                args['asignaturas'] = []
        else:
            args['asignaturas'] = obtenAsignaturas(request.session['username'])
            if not args['asignaturas']:
                args['asignaturas'] = []
        return render(request, 'coordinaAsignaturas/asignaturas.html', args)
    else:
        return redirect('/coordinaAsignaturas/login')

'''
4.  agregarAsignatura
        Permite agregar nuevas asignaturas al sistema, a la base de datos.
        Se agregan también a la coordinación.
'''
def agregarAsignatura(request):

    # Redirección si no hay sesión
    if not ('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')

    # Se intenta agregar la asignatura a la base de datos
    if request.method == 'POST':
        form = FormCrearAsignatura(request.POST,request.FILES)
        args = {'form': form}
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            # Se agrega a la coordinación
            agregaAsignaturaACoord(request.session['username'],data['codAsig'])
            args['asignaturas'] = obtenAsignaturas(request.session['username'])
            return redirect('/coordinaAsignaturas/ver')
    else:
        args = {'form': FormCrearAsignatura()}
    return render(request, 'coordinaAsignaturas/agregarAsignatura.html', args)


'''
5.  modificarAsignaturas
        Permite modificar una asignatura.
'''
def modificarAsignatura(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig = codAsig)

    # Redirección si no hay sesión
    if request.method == "POST":
        form = FormModificarAsignatura(
            request.POST,
            request.FILES,
            instance = asignatura
            )
        if form.is_valid():
            asignatura = form.save(commit = False)

            # Se actualiza la asignatura en la base de datos
            asignatura.save()
            return redirect('coordinaAsignaturas:detallesAsignatura',
                   codAsig=asignatura.codAsig)
        else :
            print("Error al modificar asignatura")
    else :
        form =  FormModificarAsignatura(instance=asignatura)
    return render(request, 'coordinaAsignaturas/modificarAsignatura.html',
                 {'form' : form})

'''
6.  eliminarAsignatura
        Eliminar una asignatura de una coordinación, mas no de la base de datos
'''
def eliminarAsignatura(request, codAsig):

    # Redirección si no hay sesión
    if not ('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')
    try:

        # La eliminamos de la coordinación únicamente
        eliminaAsignaturaDeCoord(request.session["username"],codAsig)
        return redirect('/coordinaAsignaturas/ver')
    except:
        return redirect('/coordinaAsignaturas/ver')

'''
7.  detallesAsignatura
        Muestra los detalles de una asignatura.
'''
def detallesAsignatura(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig=codAsig)
    return render(request, 'coordinaAsignaturas/detallesAsignatura.html',
                 {'asignatura' : asignatura})

'''
8.  listaTodasAsignaturas
        Muestra una lista de todas las asignaturas existentes
'''
def listaTodasAsignaturas(request):
    asignaturas = Asignatura.objects.all()

    return render(request, 'coordinaAsignaturas/listaTodasAsignaturas.html',
                 {'asignaturas' : asignaturas})

'''
9. agregarACoord
        Permite agregar una asignatura existente a la coordinación.
'''
def agregarACoord(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig = codAsig)

    # Redirección a inicio de sesión si no hay sesión
    if not ('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')
    if request.method == 'POST':
        form = FormAgregarAsignatura(request.POST, instance = asignatura)
        args = {'form': form}
        if form.is_valid():
            data = form.cleaned_data

            # Intentamos agregar la asignatura a la coordinación
            agrega = agregaAsignaturaACoord(
                request.session['username'],
                data['codAsig']
                )
            if agrega:
                args['asignaturas'] = obtenAsignaturas(
                    request.session['username']
                    )
                return redirect('/coordinaAsignaturas/ver')
        else:
            print("No se agregó la materia a la coordinacion")
    else :
        args = {'form' : FormAgregarAsignatura(instance=asignatura)}
    return render(request, 'coordinaAsignaturas/agregarAsignatura.html', args)


'''#############################################################################

                            Vistas sobre las ofertas

'''#############################################################################


'''
10. verOfertas
        Vista que muestra todas las ofertas creadas por la coordinación
'''
def verOfertas(request):

    # Obtenemos coordinación del coordinador en sesión
    s = Sesion()
    s.usuario = Usuario.objects.get(pk=request.session['username'])
    coord = s.obtenCoordinacion()

    # Se solicitan las ofertas de la coordinación en sesión
    ultimasOfertas = Oferta.objects.filter(coordinacion=coord)
    context = {
       'ultimasOfertas' : ultimasOfertas,
    }
    return render(request, 'coordinaAsignaturas/oferta.html', context)

'''
11. detallesOferta
        Se muestran las materias de la oferta y sus datos
'''
def detallesOferta(request, oferta_id):

    # Obtenemos oferta
    oferta_info = get_object_or_404(Oferta, pk=oferta_id)

    # Obtenemos sus asignaturas
    materiasOfertadas = oferta_info.asignaturas.all()
    return render(request, 'coordinaAsignaturas/detallesOferta.html',
                 {'materiasOfertadas':materiasOfertadas,'oferta_info':oferta_info})

'''
12. agregarOferta
        Permite agregar una nueva oferta
'''
def agregarOferta(request):

    # Redirección si no hay sesión
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')

    # Se envía el formulario
    if request.method == 'POST':
        # Se reproduce el formulario
        form = FormularioOferta(request.POST)
        args = {'form' : form}
        if form.is_valid():
            # se guarda la oferta sin la coordinacion
            oferta = form.save()
            # se obtiene la coordinacion del coordinador logeado
            s = Sesion()
            s.usuario = Usuario.objects.get(pk=request.session["username"])
            coord = s.obtenCoordinacion()
            # se le asigna la coordinacion a la oferta
            oferta.coordinacion = coord
            # se guarda la oferta definitivamente
            oferta.save()
            return redirect('/coordinaAsignaturas/ofertas')
    else :
        form = FormularioOferta()
        args = {'form' : form}

    return render(request, 'coordinaAsignaturas/agregarOferta.html', {'form' : form})

'''
13. modificarOferta
        Perite modificar una oferta existente
'''
def modificarOferta(request,oferta_id):

    # Redirección si no hay sesión
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')

    # Se envía el formulario
    if request.method == 'POST':
        form = FormularioOferta(request.POST,
                                instance=Oferta.objects.get(pk=oferta_id))
        args = {'form' : form}
        if form.is_valid():
            form.save()
            return redirect('coordinaAsignaturas:detallesOferta',
                            oferta_id=oferta_id)
    else :
        args = {'form' : FormularioOferta(instance=Oferta.objects.get(pk=oferta_id))}

    return render(request, 'coordinaAsignaturas/modificarOferta.html', args)


'''
14. eliminarOferta
        Elimina una oferta y redirige a la página de ver ofertas
'''
def eliminarOferta(request, oferta_id):

    # Redirección si no hay sesión
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')

    # Intentamos eliminar la oferta.
    try :
        if eliminaOferta(request.session["username"], oferta_id) :
            return redirect('/coordinaAsignaturas/ofertas')
        else :
            return redirect('/coordinaAsignaturas/login')
    except :
        return redirect('/coordinaAsignaturas/ofertas')


'''#############################################################################

            Vistas sobre la inscripción de un estudiante de postgrado

'''#############################################################################


def inscripcion(request):

    estudiante = obtenerEstudiante(request.session['username'])
    inscripciones = estudiante.inscripciones.all()
    context = {
        'estudiante' : estudiante,
        'inscripciones' : inscripciones
    }
    return render(request, 'coordinaAsignaturas/inscripcion.html', context)

'''
inscripcion: Vista de la inscripcion del estudiante
'''
def inscripcion(request):
    usuario = get_object_or_404(Estudiante, usuario=request.session['username'])
    estudiante = {'estudiante' : usuario}
    return render(request, 'coordinaAsignaturas/inscripcion.html', estudiante)
