from django import forms
from .models import Candidato
import os

def upload_directory_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "DSR_%s_%s_0.%s" % (instance.rut, instance.nombre , ext)
    return os.path.join('uploads',filename)


class Candidato_form(forms.ModelForm):

    class Meta:
        model = Candidato

        fields = [
            'nombre',
            'rut',
            'certificado_antecedentes',
            'hoja_de_vida_conductor',
            'certificado_residencia',
            'certificado_afiliacion_afp',
            'certificado_afiliacion_salud',
            'fotocopia_cedula_identidad',
            'fotocopia_licencia_conducir',
            'curriculum_vitae',
            'ultimo_finiquito',
            'documentacion_que_acredite_el_cargo',
            'certificado_estudios',
            'certificado_titulo',
            'credencial_resolucion_sns_sernageomin',
            'examen_preocupacional_salud',
            'examen_preocupacional_alcohol_drogas',
            'examen_psicosensometrico',
            'certificado_sustancias_peligrosas',
            'certificacion_rigger',
            'certificacion_pluma',
            'certificacion_choferes_operadores',
            'situacion_militar',
            'declaracion_jurada_salud',
            'odi_collahuasi_covid19',
            'reglamento_interno_excon',
            'ficha_bhp_emex',
            'odis_tortolas',
            'reglamento_conduccion_recibo_tortolas',
            'reglamento_condiccion_tortolas_anexo1',
            'solicitud_evaluacion_conduccion_tortolas',
            'odis_conduccion_qb2',
            'registro_asistencia_induccion_qb2',
            'solicitud_licencia_interna_qb2', 
            'toma_conocimiento_covid19', 
            'odis_qb22',

        ]

        labels = {
            'nombre': 'Nombre',
            'rut': 'Rut',
            'certificado_antecedentes': 'Certificado Antecedentes',
            'hoja_de_vida_conductor': 'Hoja de vida del conductor',
            'certificado_residencia': 'Certificado de residencia',
            'certificado_afiliacion_afp': 'Certificado afiliación AFP',
            'certificado_afiliacion_salud': 'Certificado afiliacion de salud',
            'fotocopia_cedula_identidad': 'Fotocopia de cedula de identidad',
            'fotocopia_licencia_conducir': 'Fotocopia de licencia de conducir',
            'curriculum_vitae': 'Curriculum vitae',
            'ultimo_finiquito': 'Ultimo finiquito',
            'documentacion_que_acredite_el_cargo': 'Documentacion que acredite el cargo',
            'certificado_estudios': 'Certificado de estudios',
            'certificado_titulo': 'Certificado de titulo',
            'credencial_resolucion_sns_sernageomin': 'Credencial resolución sns sernageomin',
            'examen_preocupacional_salud': 'Examen preocupacional de salud',
            'examen_preocupacional_alcohol_drogas': 'Examen preocupacional alcohol drogas',
            'examen_psicosensometrico': 'Examen psicosensometrico',
            'certificado_sustancias_peligrosas': 'Certificado sustancias peligrosas',
            'certificacion_rigger': 'Certificación rigger',
            'certificacion_pluma': 'Certificación pluma',
            'certificacion_choferes_operadores': 'Certificación choferes operadores',
            'situacion_militar': 'Situacion militar',
            'declaracion_jurada_salud': 'Declaración jurada de salud',
            'odi_collahuasi_covid19': 'Odi Collahuasi covid19',
            'reglamento_interno_excon': 'Reglamento interno Excon',
            'ficha_bhp_emex': 'Ficha BHP Emex',
            'odis_tortolas': 'Odis Tortolas',
            'reglamento_conduccion_recibo_tortolas': 'Reglamento de conducción recibo Tortolas',
            'reglamento_conduccion_tortolas_anexo1': 'Reglamento de conducción Tortolas anexo1',
            'solicitud_evaluacion_conduccion_tortolas': 'Solicitud evaluacion conducción Tortolas',
            'odis_conduccion_qb2': 'Odis conducción QB2',
            'registro_asistencia_induccion_qb2': 'Registro de asistencia inducción QB2',
            'solicitud_licencia_interna_qb2': 'Solicitud licencia interna QB2', 
            'toma_conocimiento_covid19': 'Toma conocimiento covid19', 
            'odis_qb22': 'Odis QB22',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'rut': forms.TextInput(attrs={'class':'form-control'}),
            'certificado_antecedentes': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'hoja_de_vida_conductor': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'certificado_residencia': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'certificado_afiliacion_afp': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'certificado_afiliacion_salud': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'fotocopia_cedula_identidad': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'fotocopia_licencia_conducir': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'curriculum_vitae': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'ultimo_finiquito': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'documentacion_que_acredite_el_cargo': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'certificado_estudios': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'certificado_titulo': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'credencial_resolucion_sns_sernageomin': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'examen_preocupacional_salud': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'examen_preocupacional_alcohol_drogas': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'examen_psicosensometrico': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'certificado_sustancias_peligrosas': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'certificacion_rigger': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'certificacion_pluma': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'certificacion_choferes_operadores': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'situacion_militar': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'declaracion_jurada_salud': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'odi_collahuasi_covid19': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'reglamento_interno_excon': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'ficha_bhp_emex': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'odis_tortolas': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'reglamento_conduccion_recibo_tortolas': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'reglamento_condiccion_tortolas_anexo1': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'solicitud_evaluacion_conduccion_tortolas': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'odis_conduccion_qb2': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'registro_asistencia_induccion_qb2': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
            'solicitud_licencia_interna_qb2': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}), 
            'toma_conocimiento_covid19': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}), 
            'odis_qb22': forms.ClearableFileInput(attrs={"multiple":True, 'class':'form-control'}),
        }

        def clean_name(self):
            name = self.cleaned_data['nombre']
            if len(name) < 2:
                raise forms.ValidationError("Name must be at least 2 characters long.")
            return name

        def clean_id(self):
            id = self.cleaned_data['rut']
            if len(id) < 2:
                raise forms.ValidationError("ID must be at least 2 characters long.")
            return id