# -*- coding: utf-8 -*-


from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from coordinaAsignaturas.models import Usuario, Asignatura, Oferta
import hashlib, datetime
import re

fecha = datetime.datetime.now()

'''

Universidad Simón Bolívar
Ingeniería de Software I CI-3715
Sistema de gestión de postgrados de la USB

Vistas de coordinaAsignaturas

Desarrollado por Equipo Null Pointer Exception


 Indice de vistas:
      1.  LoginForm
      2.  FormularioAsignatura.
      3.  FormularioCrearAsignatura.
      4.  FormularioModificarAsignatura.
      5.  FormularioAgregarAsignatura.
      6.  FormularioOferta.
      7.  FormularioModificarAsignatura.
      8.  FormCrearOferta
'''

'''
1. LoginForm
    Formulario que se encarga de registrar al usuario
'''
class LoginForm(forms.Form):
    username = forms.EmailField(max_length = 30)
    password = forms.CharField(max_length = 64, widget = forms.PasswordInput)

    def clean(self):
        limpio = super(LoginForm, self).clean()
        usr = limpio.get('username')
        pwd = limpio.get('password')
        try:
            busqueda = Usuario.objects.get(pk = usr)
            hashm = hashlib.sha256()
            pswd = str.encode(pwd)
            hashm.update(pswd)

            if hashm.hexdigest() != busqueda.password:
                self.add_error('username', 'Usuario o clave incorrecto')
        except:
            self.add_error('username', 'Usuario o clave incorrecto')
        return limpio

    class Meta:
        model = Usuario
        exlude = []

'''
2. FormularioAsignatura
    Formulario base para los fomularios de agregar, crear y modificar
'''
class FormularioAsignatura(forms.ModelForm):
    lun = forms.BooleanField(required = False)
    lun_inicio = forms.ChoiceField(choices = [(n, n) for n in range(1, 11)])
    lun_fin = forms.ChoiceField(choices = [(n, n) for n in range(1, 11)])
    mar = forms.BooleanField(required = False)
    mar_inicio = forms.ChoiceField(choices = [(n, n) for n in range(1, 11)])
    mar_fin = forms.ChoiceField(choices = [(n, n) for n in range(1, 11)])
    mie = forms.BooleanField(required = False)
    mie_inicio = forms.ChoiceField(choices = [(n, n) for n in range(1, 11)])
    mie_fin = forms.ChoiceField(choices = [(n, n) for n in range(1, 11)])
    jue = forms.BooleanField(required = False)
    jue_inicio = forms.ChoiceField(choices = [(n, n) for n in range(1, 11)])
    jue_fin = forms.ChoiceField(choices = [(n, n) for n in range(1, 11)])
    vie = forms.BooleanField(required = False)
    vie_inicio = forms.ChoiceField(choices = [(n, n) for n in range(1, 11)])
    vie_fin = forms.ChoiceField(choices = [(n, n) for n in range(1, 11)])

    class Meta:
        model = Asignatura
        exclude = ['diaHora']
        fields = [
            'codAsig',
            'creditos',
            'nomAsig',
            'progAsig',
            'prof',
            'codDpto',
            'vista',
        ]
        labels = {'codAsig': 'Codigo de asignatura',
                  'creditos': 'Numero de creditos',
                  'nomAsig': 'Nombre',
                  'progAsig': 'Programa',
                  'prof': 'Profesor',
                  'codDpto': 'Departamento',
                  'vista': 'Vista'}
        widgets = {
            'codAsig': forms.TextInput(attrs = {'class': 'form-control'}),
            'creditos': forms.Select(attrs = {'class': 'form-control'}),
            'nomAsig': forms.TextInput(attrs = {'class': 'form-control'}),
            'prof': forms.Select(attrs = {'class': 'form-control'}),
            'codDpto': forms.Select(attrs = {'class': 'form-control'})
        }

    # Haciendole override al metodo clean
    def clean(self):
        regexCodigo = '^([A-Z]{2,2})(\-){0,1}([0-9]{4,4})$'
        mensajeErrorCodigo = 'El codigo debe ser dos letras mayusculas y cuatro digitos separados, o no, por un guion'
        regexNombre = '^[a-záéíóúäëïöüA-ZÁÉÍÓÚÄËÏÖÜ0-9ñ¿?¡!\ ]{0,80}$'
        mensajeErrorNombre = 'El nombre de la materia no es valido'
        mensajeErrorIntervalo = 'El intervalo de tiempo debe ser positivo'
        mensajeErrorLimites = 'Debe indicarse el inicio y la finalizacion'
        try:
            limpio = super(FormularioAsignatura, self).clean()
            codigo = limpio.get('codAsig')
            cod = re.compile(regexCodigo)
            if cod.match(codigo) == None:
                self.add_error('codAsig', mensajeErrorCodigo)
                return limpio
            nombre = limpio.get('nomAsig')
            nom = re.compile(regexNombre)
            if nom.match(nombre) == None:
                self.add_error('nomAsig', mensajeErrorNombre)
                return limpio
            dias = ['lun','mar','mie','jue','vie']
            d = False
            for dia in dias:
                d = d or limpio.get(dia)
            if not (d):
                self.add_error('lun', 'Debe haber al menos un dia de clases')
                return limpio
            for dia in dias:
                if  limpio.get(dia) == False:
                    continue
                try:
                    inicio = int(limpio.get(dia + "_inicio"))
                    fin    = int(limpio.get(dia + "_fin"))
                    if inicio > fin:
                        self.add_error(dia + '_inicio', mensajeErrorIntervalo)
                except:
                    self.add_error(dia + '_inicio', mensajeErrorLimites)
        except:
            pass
        return limpio

    # Haciendo overwrite a la funcion de save #
    def save(self, commit = True):
        asignatura = super(FormularioAsignatura, self).save(commit = False)
        dias = ['lun','mar','mie','jue','vie']
        dias_clase = []
        for dia in dias:
            if self.cleaned_data[dia]:
                dias_clase.append(dia)
        horarios = [
            "%s %s-%s" % (
                dia,
                self.cleaned_data[dia + '_inicio'],
                self.cleaned_data[dia + '_fin']
                )
            for dia in dias_clase
            ]
        asignatura.diaHora = " ; ".join(horarios)
        if commit:
            asignatura.save()
        return asignatura

'''
3. FormCrearAsignatura
    Fomulario que se encarga de crear una nueva asignatura en el sistema
'''
class FormCrearAsignatura(FormularioAsignatura):
    def clean(self):
        limpio = super(FormCrearAsignatura, self).clean()
        codigo = limpio.get('codAsig')
        nombre = limpio.get('nomAsig')
        # Comprobando que no haya una asignatura con igual codigo
        try:
            Asignatura.objects.get(codAsig = codigo)
            self.add_error(
                'codAsig',
                'Ya existe una asignatura con ese codigo'
                )
        except Asignatura.DoesNotExist:
            pass

        # Comprobando que no haya una asignatura con igual nombre
        try:
            Asignatura.objects.get(nomAsig = nombre)
            self.add_error(
                'nomAsig',
                'Ya existe una asignatura con ese nombre'
                )
        except Asignatura.DoesNotExist:
            pass

        return limpio

'''
4. FormModificarAsignatura
    Formulario que se encarga de registrar cambios a una asignatura
'''
class FormModificarAsignatura(FormularioAsignatura):

    def __init__(self, *args, **kwargs):
        super(FormModificarAsignatura, self).__init__(*args, **kwargs)
        codAsig = getattr(self, 'codAsig', None)
        self.fields['codAsig'].widget.attrs['readonly'] = True
        labels = {'codAsig': 'Codigo de asignatura',
                  'creditos': 'Numero de creditos',
                  'nomAsig': 'Nombre',
                  'progAsig': 'Programa',
                  'prof': 'Profesor',
                  'codDpto': 'Departamento',
                  'vista': 'Vista'}
        widgets = {
            'codAsig': forms.TextInput(attrs = {'class': 'form-control'}),
            'creditos': forms.Select(attrs = {'class': 'form-control'}),
            'nomAsig': forms.TextInput(attrs = {'class': 'form-control'}),
            'progAsig': forms.TextInput(attrs = {'class': 'form-control'}),
            'prof': forms.Select(attrs = {'class': 'form-control'}),
            'codDpto': forms.Select(attrs = {'class': 'form-control'})
        }
        try:
            if kwargs is not None and "instance" in kwargs.keys():
                horario = kwargs["instance"].diaHora
                horario = horario.split(" ; ")
                for hora in horario:
                    if hora != "":
                        hora = hora.split(" ")
                        hora[1] = hora[1].split("-")
                        self.fields[hora[0]].initial = True
                        inicio = "%s_inicio" % (hora[0])
                        fin    = "%s_fin" % (hora[0])
                        self.fields[inicio].initial = int(hora[1][0])
                        self.fields[fin].initial = int(hora[1][1])
        except:
            pass

'''
5. FormAgregarAsignatura
    Formulario que se encarga de agregar una materia existente a la coordinacion
'''
class FormAgregarAsignatura(FormularioAsignatura):
    def clean(self):
        limpio = super(FormAgregarAsignatura, self).clean()
        codigo = limpio.get('codAsig')
        nombre = limpio.get('nomAsig')
        return limpio

'''
6. FormularioOferta
    Formulario base para la creacion y modificacion de una oferta
'''
class FormularioOferta(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormularioOferta, self).__init__(*args, **kwargs)
        self.fields['asignaturas'].widget = CheckboxSelectMultiple()
        self.fields['asignaturas'].queryset = Asignatura.objects.all()

    class Meta:
        model = Oferta
        exclude = []
        fields = [
            'trimestre',
            'asignaturas',
            'anio'
        ]
        labels = {
            'trimestre': 'Trimestre',
            'asignaturas': 'Asignaturas',
            'anio': 'Periodo',
        }
        widgets = {
            'trimestre': forms.Select(attrs = {'class': 'form-control'}),
            'anio': forms.TextInput(attrs = {'class': 'form-control'}),
            'asignaturas': forms.Select(attrs = {
                'class': 'form-control text-center',
                'multiple': 'multiple'
                }
            )
        }

'''
7. FormModificarOferta
    Formulario que se encarga de modificar una oferta existente
'''
class FormModificarOferta(FormularioOferta):
    def __init__(self, *args, **kwargs):
        super(FormModificarOferta, self).__init__(*args, **kwargs)
        self.fields['asignaturas'].widget = CheckboxSelectMultiple()
        self.fields['asignaturas'].queryset = Asignatura.objects.all()
        labels = {
            'trimestre': 'Trimestre',
            'asignaturas': 'Asignaturas',
            'anio': 'Periodo',
        }
        widgets = {
            'trimestre': forms.Select(attrs = {'class': 'form-control'}),
            'anio': forms.TextInput(attrs = {'class': 'form-control'}),
            'asignaturas': forms.Select(attrs = {
                'class': 'form-control text-center',
                'multiple': 'multiple'
                }
            )
        }

'''
8. FromCrearOferta
    Formulario que se encarga de registrar una nueva oferta a la coordinacion
'''
class FormCrearOferta(FormularioOferta):
    pass