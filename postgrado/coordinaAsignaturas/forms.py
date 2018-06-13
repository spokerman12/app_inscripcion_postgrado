# -*- coding: utf-8 -*-


from django import forms
from coordinaAsignaturas.models import *
import hashlib

# Formulario de registro #
class LoginForm(forms.Form) :
    username = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)

    def clean(self):
        limpio = super(LoginForm, self).clean()
        usr = limpio.get('username')
        pwd = limpio.get('password')
        try:
            q = Usuario.objects.get(pk=usr)
            m = hashlib.sha256()
            p = str.encode(pwd)
            m.update(p)
            if (m.hexdigest()==q.password):
                pass
                #self.usuario = q
            else:
                self.add_error('username', 'Usuario o clave incorrecto')
        except Usuario.DoesNotExist:
            self.add_error('username', 'Usuario o clave incorrecto')
        return limpio

# Formulario base de una asignatura #
class FormularioAsignatura(forms.ModelForm):
    lun = forms.BooleanField(required=False)
    lun_inicio = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    lun_fin = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    mar = forms.BooleanField(required=False)
    mar_inicio = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    mar_fin = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    mie = forms.BooleanField(required=False)
    mie_inicio = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    mie_fin = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    jue = forms.BooleanField(required=False)
    jue_inicio = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    jue_fin = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    vie = forms.BooleanField(required=False)
    vie_inicio = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    vie_fin = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    
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
        labels = {'codAsig' : 'Codigo de asignatura',
                  'creditos' : 'Numero de creditos',
                  'nomAsig' : 'Nombre',
                  'progAsig' : 'Programa',
                  'prof' : 'Profesor',
                  'codDpto': 'Departamento',
                  'vista' : 'Vista'}
        widgets = {
            'codAsig' : forms.TextInput(attrs = {'class':'form-control'}),
            'creditos' : forms.Select(attrs = {'class':'form-control'}),
            'nomAsig' : forms.TextInput(attrs = {'class':'form-control'}),
            'progAsig' : forms.TextInput(attrs = {'class':'form-control'}),
            'prof' : forms.Select(attrs = {'class':'form-control'}),
            'codDpto' : forms.Select(attrs = {'class':'form-control'})
        }
    # Haciendole override al metodo clean
    def clean(self):
        
        limpio = super(FormularioAsignatura, self).clean()
        codigo = limpio.get('codAsig')
        nombre = limpio.get('nomAsig')
        dias = ['lun','mar','mie','jue','vie']
        d = False
        for dia in dias :
            d = d or limpio.get(dia)
        if not(d) :
            self.add_error('lun', 'Debe haber al menos un dia de clases')
            return limpio
        
        for dia in dias :
            if  limpio.get(dia) == False :
                continue
            if int(limpio.get(dia+"_inicio")) > int(limpio.get(dia+"_fin")) :
                self.add_error(dia+'_inicio', 'El intervalo de tiempo debe ser positivo')
        
        return limpio
    
    def save(self, commit=True):
        asignatura = super(FormularioAsignatura, self).save(commit=False)
        dias = ['lun','mar','mie','jue','vie']
        dias_clase = []
        for dia in dias :
            if self.cleaned_data[dia] :
                dias_clase.append(dia)
        s = [dia+" "+self.cleaned_data[dia+'_inicio']+"-"+self.cleaned_data[dia+'_fin'] for dia in dias_clase]
        asignatura.diaHora = " ; ".join(s)
        if commit:
            asignatura.save()
        return asignatura

# Formulario para crear una nueva asignatura #
class FormCrearAsignatura(FormularioAsignatura) :
    def clean(self) :
        limpio = super(FormCrearAsignatura, self).clean()
        codigo = limpio.get('codAsig')
        nombre = limpio.get('nomAsig')
        # Comprobando que no haya una asignatura con igual codigo
        try:
            Asignatura.objects.get(codAsig=codigo)
            self.add_error('codAsig', 'Ya existe una asignatura con ese codigo')
        except Asignatura.DoesNotExist :
            pass
       
        # Comprobando que no haya una asignatura con igual nombre
        try:
            Asignatura.objects.get(nomAsig=nombre)
            self.add_error('nomAsig', 'Ya existe una asignatura con ese nombre')
        except Asignatura.DoesNotExist :
            pass

        return limpio

# Formulario para Modificar una asignatura #
class FormModificarAsignatura(FormularioAsignatura) :
    
    def __init__(self, *args, **kwargs):
        super(FormModificarAsignatura, self).__init__(*args, **kwargs)
        codAsig = getattr(self, 'codAsig', None)
        self.fields['codAsig'].widget.attrs['readonly'] = True
        labels = {'codAsig' : 'Codigo de asignatura',
                  'creditos' : 'Numero de creditos',
                  'nomAsig' : 'Nombre',
                  'progAsig' : 'Programa',
                  'prof' : 'Profesor',
                  'codDpto': 'Departamento',
                  'vista' : 'Vista'}
        widgets = {
            'codAsig' : forms.TextInput(attrs = {'class':'form-control'}),
            'creditos' : forms.Select(attrs = {'class':'form-control'}),
            'nomAsig' : forms.TextInput(attrs = {'class':'form-control'}),
            'progAsig' : forms.TextInput(attrs = {'class':'form-control'}),
            'prof' : forms.Select(attrs = {'class':'form-control'}),
            'codDpto' : forms.Select(attrs = {'class':'form-control'})
        }

# Formulario para agregar una asignatura a la coordinacion #
class FormAgregarAsignatura(FormularioAsignatura) :
    def clean(self) :
        limpio = super(FormAgregarAsignatura, self).clean()
        codigo = limpio.get('codAsig')
        nombre = limpio.get('nomAsig')

        return limpio

# Formulario para agregar una nueva oferta #
class FormCrearOferta(forms.ModelForm):
    class Meta:
        model = Oferta
        exclude = []

        labels = {
            'coordinacion' : 'Coordinacion',
            'trimestre' : 'Trimestre',
            'asignaturas' : 'Asignaturas',
            'anio' : 'Periodo',
        }

        