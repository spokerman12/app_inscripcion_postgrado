# -*- coding: utf-8 -*-
#   Vistas de la aplicacion.
#
#   Indice de vistas:
#       1.  home.
#       2.  principal.
#       3.  verOfertas.
#       4.  detallesOferta.
#       5.  agregarOferta.
#       6.  modificarOferta.
#       7.  verAsignaturas.
#       8.  eliminarOferta.
#       9.  verAsignaturas.
#       10. agregarAsignatura.
#       11. modificarAsignatura.
#       12. eliminarAsignatura.
#       13. detallesAsignatura.
#       14. listaTodasAsignaturas.
#       15. agregarACoord.

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LoginForm, FormCrearOferta, FormCrearAsignatura
from .forms import FormModificarOferta, FormAgregarAsignatura
from .models import Oferta, Usuario, Sesion, Asignatura 
from .models import agregaAsignaturaACoord, eliminaOferta, obtenAsignaturas
from .models import eliminaAsignaturaDeCoord

# Funcion home: muestra la pantalla de inicio de la aplicacion, presenta el
# formulario de inicio de sesion para la aplicacion.
def home(request: HttpRequest) -> HttpResponse:
    login     = 'coordinaAsignaturas/login.html'
    principal = '/coordinaAsignaturas/principal'
    if request.method == "POST" :   
        form = LoginForm(request.POST)
        args = {'form': form}
        if form.is_valid() :
            request.session['username'] = form.cleaned_data['username']
            return redirect(principal)
    else :
        args = {'form': LoginForm()}
    return render(request, login, args)

# Funcion principal: muestra la pantalla de inicio, despues de la autenticacion
# del usuario.
def principal(request: HttpRequest) -> HttpResponse:
    initIndex = 'coordinaAsignaturas/initIndex.html'
    asignaturas = Asignatura.objects.all()
    context = {'asignaturas' : asignaturas}
    return render(request, initIndex, context)

# Funcion verOfertas: muestra las ofertas registradas para el usuario que se ha
# autenticado.
def verOfertas(request: HttpRequest) -> HttpResponse:
    oferta = 'coordinaAsignaturas/oferta.html'
    sesion = Sesion()
    sesion.usuario = Usuario.objects.get(pk = request.session['username'])
    coord = sesion.obtenCoordinacion()
    ultimasOfertas = Oferta.objects.filter(coordinacion = coord)
    context = {
       'ultimasOfertas' : ultimasOfertas,
    }
    return render(request, oferta, context)

# Funcion detallesOferta: muestra las materias registradas en la oferta que ha
# sido seleccionada en la base de datos por su clave: oferta_id.
def detallesOferta(request: HttpRequest, oferta_id: int) -> HttpResponse:
    detallesOferta = 'coordinaAsignaturas/detallesOferta.html'
    oferta_info = get_object_or_404(Oferta, pk = oferta_id)
    materiasOfertadas = oferta_info.asignaturas.all()
    context = {
        'materiasOfertadas': materiasOfertadas,
        'oferta_info': oferta_info
    }
    return render(request, detallesOferta, context)

# Funcion agregarOferta: despliega el formulario para crear una nueva oferta en
# el espacio del usuario autenticado.
def agregarOferta(request: HttpRequest) -> HttpResponse:
    login         = '/coordinaAsignaturas/login'
    ofertas       = '/coordinaAsignaturas/ofertas'
    agregarOferta = 'coordinaAsignaturas/agregarOferta.html'
    form = FormCrearOferta(request.POST)
    if not('username' in request.session.keys()):
        return redirect(login)
    if request.method == 'POST':
        form = FormCrearOferta(request.POST)
        args = {'form' : form}
        if form.is_valid():
            form.save()
            return redirect(ofertas)
    else :
        args = {'form' : FormCrearAsignatura()}
    context = {
        'form': form
    }
    return render(request, agregarOferta, context)

# Funcion modificarOferta: accede a la oferta que ha sido seleccionada en la
# base de datos por su clave: oferta_id y redirige a la vista para modificarla.
def modificarOferta(request: HttpRequest, oferta_id: int) -> HttpResponse:
    login           = '/coordinaAsignaturas/login'
    detallesOferta  = 'coordinaAsignaturas:detallesOferta'
    modificarOferta = 'coordinaAsignaturas/modificarOferta.html'
    oferta = Oferta.objects.get(pk=oferta_id)
    detallesOferta
    if not('username' in request.session.keys()):
        return redirect(login)
    if request.method == 'POST':
        form = FormModificarOferta(request.POST, instance = oferta)
        args = {'form' : form}
        if form.is_valid():
            form.save()
            return redirect(detallesOferta, oferta_id = oferta_id)
        else :
            print("Error al modificar oferta")
    else :
        args = {'form' : FormModificarOferta(instance = ofertas)}
    return render(request, modificarOferta, args)

# Funcion eliminarOferta: elimina la oferta senalada por oferta_id de la base
# de datos.
def eliminarOferta(request: HttpRequest, oferta_id: int) -> HttpResponse:
    login = '/coordinaAsignaturas/login'
    ofertas = '/coordinaAsignaturas/ofertas'
    if not('username' in request.session.keys()):
        return redirect(login)
    try :
        if eliminaOferta(request.session["username"], oferta_id) :
            return redirect(ofertas)
        else :
            return redirect(login)
    except :
        return redirect(ofertas)

# Funcion verAsignaturas: permite visualizar las asignaturas dentro de la
# coordinacion.
def verAsignaturas(request: HttpRequest) -> HttpResponse:
    asignaturas = 'coordinaAsignaturas/asignaturas.html'
    if 'username' in request.session.keys():
        args = {'usuario': request.session['username']}
        if request.method == 'POST' :
            try:
                return render(request, asignaturas, args)
            except:
                args['asignaturas'] = []
        else :
            args['asignaturas'] = obtenAsignaturas(request.session['username'])
            if not args['asignaturas']:
                args['asignaturas'] = []
        return render(request, asignaturas, args)
    else :
        return redirect('login')

# Funcion agregarAsignatura: agregar una asignatura nueva a la base de datos y
# la muestra en la vista.
def agregarAsignatura(request: HttpRequest) -> HttpResponse:
    login             = '/coordinaAsignaturas/login'
    vista             = '/coordinaAsignaturas/ver'
    agregarAsignatura = 'coordinaAsignaturas/agregarAsignatura.html'
    usuario = 'username' in request.session.keys()
    if not usuario:
        return redirect(login)
    if request.method == 'POST':
        form = FormCrearAsignatura(request.POST)
        args = {'form' : form}
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            username = request.session['username']
            codAsig = data['codAsig']
            agregaAsignaturaACoord(username, codAsig)
            args['asignaturas'] = obtenAsignaturas(username)
            return redirect(vista)
    else :
        args = {'form' : FormCrearAsignatura()}
    return render(request, agregarAsignatura, args)

# Funcion modificarAsignatura: Modifica los datos de la asignatura de codigo
# codAsig, existente en la base de datos.
def modificarAsignatura(request: HttpRequest, codAsig: str) -> HttpResponse:
    detallesAsignatura  = 'coordinaAsignaturas:detallesAsignatura'
    modificarAsignatura = 'coordinaAsignaturas/modificarAsignatura.html'
    asignatura = get_object_or_404(Asignatura, codAsig = codAsig)
    if request.method == "POST":
        form = FormModificarAsignatura(request.POST, instance = asignatura)
        if form.is_valid():
            asignatura = form.save(commit = False)
            asignatura.save()
            return redirect(detallesAsignatura, codAsig = asignatura.codAsig)
        else :
            print("Error al modificar asignatura")
    else :
        form =  FormModificarAsignatura(instance = asignatura)
    context = {'form' : form}
    return render(request, modificarAsignatura, context)

# Funcion eliminarAsignatura: Elimina la asignatura de codigo codAsig de la
# coordinacion.
def eliminarAsignatura(request: HttpRequest, codAsig: str) -> HttpResponse:
    login = '/coordinaAsignaturas/login'
    vista = '/coordinaAsignaturas/ver'
    usuario = 'username' in request.session.keys()
    if not usuario:
        return redirect()
    try :
        eliminaAsignaturaDeCoord(request.session["username"], codAsig)
        return redirect(vista)
    except :
        return redirect(vista)

# Funcion detallesAsignatura: Muestra los detalles de la asignatura de codigo
# codAsig.
def detallesAsignatura(request: HttpRequest, codAsig: str) -> HttpResponse:
    detallesAsignatura = 'coordinaAsignaturas/detallesAsignatura.html'
    asignatura         = get_object_or_404(Asignatura, codAsig = codAsig)
    context            = {'asignatura': asignatura}
    return render(request, detallesAsignatura, context)

# Funcion listaTodasAsignaturas: Despliega una lista de todas las asignaturas
# existentes en la base de datos.
def listaTodasAsignaturas(request: HttpRequest) -> HttpResponse:
    listaTodasAsignaturas = 'coordinaAsignaturas/listaTodasAsignaturas.html'
    asignaturas           = Asignatura.objects.all()
    context               = {'asignaturas': asignaturas}
    return render(request, listaTodasAsignaturas, context)

# Funcion agregarACoord: Agrega la asignatura de codigo codAsig a la
# coordinacion.
def agregarACoord(request: HttpRequest, codAsig: str) -> HttpResponse:
    login             = '/coordinaAsignaturas/login'
    vista             = '/coordinaAsignaturas/ver'
    agregarAsignatura = 'coordinaAsignaturas/agregarAsignatura.html'
    asignatura = get_object_or_404(Asignatura, codAsig = codAsig)
    usuario = 'username' in request.session.keys()
    if not usuario:
        return redirect(login)
    if request.method == 'POST':
        form = FormAgregarAsignatura(request.POST, instance = asignatura)
        args = {'form' : form}
        if form.is_valid():
            # form.save()
            data = form.cleaned_data
            username = request.session['username']
            codAsig  = data['codAsig']
            if (agregaAsignaturaACoord(username, codAsig)):
                args['asignaturas'] = obtenAsignaturas(username)
                return redirect(vista)
        else :
            print("No se agrego la materia a la coordinacion")
    else :
        args = {'form' : FormAgregarAsignatura(instance = asignatura)}
    return render(request, agregarAsignatura, args)