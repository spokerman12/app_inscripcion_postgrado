'''

Universidad Simón Bolívar
Ingeniería de Software I CI-3715
Sistema de gestión de postgrados de la USB

Vistas de coordinaAsignaturas

Desarrollado por Equipo Null Pointer Exception

'''

# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import *
from .forms import *


'''
home: Vista que representa la página de inicio de sesión
'''
def home(request):


    if request.method == "POST" :

        # Si hace POST, recibimos el formulario
        form = LoginForm(request.POST)
        args = {'form': form}

        # Se verifica si el form es válido. Ver form.is_valid en forms.py
        if form.is_valid() :
            #request.session['username'] = form.cleaned_data['username']
            #print(request.session['username'])
            #if esEstudiante(request.session['username']):
                #return render(request, 'coordinaAsignaturas/login.html', args)
            #else:  
                # return redirect('/coordinaAsignaturas/ver')
                return redirect('/coordinaAsignaturas/principal')
    else :

        # Primero se reproduce el formulario
        args = {'form': LoginForm()}
    return render(request, 'coordinaAsignaturas/login.html', args)


'''
principal: Vista que representa la página principal para el coordinador
'''
def principal(request):

    # Solicitamos todas las asignaturas a la base de datos
    asignaturas = Asignatura.objects.all()
    context = {'asignaturas' : asignaturas}
    return render(request, 'coordinaAsignaturas/initIndex.html', context)

'''
verOfertas: Vista que representa la página de inicio de sesión
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
detallesOferta: Se muestran las materias de la oferta y sus datos
'''
def detallesOferta(request, oferta_id):

    # Obtenemos oferta
    oferta_info = get_object_or_404(Oferta, pk=oferta_id)

    # Obtenemos sus asignaturas
    materiasOfertadas = oferta_info.asignaturas.all()
    return render(request, 'coordinaAsignaturas/detallesOferta.html', 
                 {'materiasOfertadas':materiasOfertadas,'oferta_info':oferta_info})

'''
agregarOferta: Permite agregar una nueva oferta
'''
def agregarOferta(request):

    # Se reproduce el formulario
    form = FormCrearOferta(request.POST)

    # Redirección si no hay sesión
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')

    # Se envía el formulario
    if request.method == 'POST':
        form = FormCrearOferta(request.POST)
        args = {'form' : form}
        if form.is_valid():
            form.save()

            return redirect('/coordinaAsignaturas/ofertas')
    else :
        args = {'form' : FormCrearAsignatura()}

    return render(request, 'coordinaAsignaturas/agregarOferta.html', {'form' : form})

'''
modificarOferta: Perite modificar una oferta existente
'''
def modificarOferta(request,oferta_id):

    # Redirección si no hay sesión
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')

    # Se envía el formulario
    if request.method == 'POST':
        form = FormModificarOferta(request.POST, instance=Oferta.objects.get(pk=oferta_id))
        args = {'form' : form}
        if form.is_valid():
            form.save()
            return redirect('coordinaAsignaturas:detallesOferta', oferta_id=oferta_id)
        else :
            print("Error al modificar oferta")
    else :
        args = {'form' : FormModificarOferta(instance=Oferta.objects.get(pk=oferta_id))}

    return render(request, 'coordinaAsignaturas/modificarOferta.html', args)


'''
eliminarOferta: Elimina una oferta y redirige al usuario
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

'''
verAsignaturas: Vista que muestra las asignaturas de la coordinación
'''
def verAsignaturas(request):

    # Redirección si no hay sesión
    if 'username' in request.session.keys():
        args = {'usuario' : request.session['username']
                }
        # Se pasa un request con las asignaturas en args
        if request.method == 'POST' :
            try:
                return render(request, 'coordinaAsignaturas/asignaturas.html', 
                              args)
            except:
                args['asignaturas'] = []
        else :
            args['asignaturas'] = obtenAsignaturas(request.session['username'])
            if not args['asignaturas'] :
                args['asignaturas'] = []
        return render(request, 'coordinaAsignaturas/asignaturas.html', args)
    else :
        return redirect('login')

'''
agregarAsignatura: Permite agregar nuevas asignaturas al sistema.
                   Se agregan también a la coordinación
'''
def agregarAsignatura(request):

    # Redirección si no hay sesión
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')

    # Se intenta agregar la asignatura a la base de datos
    if request.method == 'POST':
        form = FormCrearAsignatura(request.POST)
        args = {'form' : form}
        if form.is_valid():
            form.save()
            data = form.cleaned_data

            # Se agrega a la coordinación
            agregaAsignaturaACoord(request.session['username'],data['codAsig'])
            args['asignaturas'] = obtenAsignaturas(request.session['username'])
            return redirect('/coordinaAsignaturas/ver')
    else :
        args = {'form' : FormCrearAsignatura()}
    return render(request, 'coordinaAsignaturas/agregarAsignatura.html', args)


'''
modificarAsignaturas: Permite modificar una asignatura.
'''
def modificarAsignatura(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig=codAsig)

    # Redirección si no hay sesión
    if request.method == "POST":
        form = FormModificarAsignatura(request.POST, instance=asignatura)
        if form.is_valid():
            asignatura = form.save(commit=False)

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
eliminarAsignatura: Eliminar una asignatura (de una coordinación).

'''
def eliminarAsignatura(request, codAsig):

    # Redirección si no hay sesión
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')
    try :

        # La eliminamos de la coordinación únicamente
        eliminaAsignaturaDeCoord(request.session["username"],codAsig)
        return redirect('/coordinaAsignaturas/ver')
    except :
        return redirect('/coordinaAsignaturas/ver')

'''
detallesAsignatura: Genera el template de detalles de una asignatura.
                    Las pasa por request
'''
def detallesAsignatura(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig=codAsig)
    return render(request, 'coordinaAsignaturas/detallesAsignatura.html', 
                 {'asignatura' : asignatura})


'''
listaTodasAsignaturas: Genera el template con todas las asignaturas existentes
                       Las pasa por request
'''
def listaTodasAsignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'coordinaAsignaturas/listaTodasAsignaturas.html', 
                 {'asignaturas' : asignaturas})



'''
agregarACoord: Instanciando un formulario, permite agregar 
               una asignatura a la coordinación.
'''
def agregarACoord(request, codAsig):
    asignatura = get_object_or_404(Asignatura, codAsig=codAsig)

    # Redirección si no hay sesión
    if not('username' in request.session.keys()):
        return redirect('/coordinaAsignaturas/login')
    if request.method == 'POST':
        form = FormAgregarAsignatura(request.POST, instance=asignatura)
        args = {'form' : form}
        if form.is_valid():
            data = form.cleaned_data

            # Intentamos agregar la asignatura a la coordinación
            if (agregaAsignaturaACoord(request.session['username'],data['codAsig'])):
                args['asignaturas'] = obtenAsignaturas(request.session['username'])
                return redirect('/coordinaAsignaturas/ver')
        else :
            print("No se agregó la materia a la coordinacion")
    else :
        args = {'form' : FormAgregarAsignatura(instance=asignatura)}
    return render(request, 'coordinaAsignaturas/agregarAsignatura.html', args)