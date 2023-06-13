from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect
from candidato.models import Candidato
from .forms import Candidato_form
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

def upload_directory_name(instance, filename):
    ext = filename.split('.')[-1]
    form=Candidato_form.objects.get(id=instance.form.id)
    filename = "DSR_%s_%s_0.%s" % (instance.rut, instance.form.label , ext)
    return os.path.join('uploads',filename)

class CandidatoList(ListView):
	model = Candidato
	template_name = 'candidato/candidato_list.html'
	paginate_by = 2

class CandidatoCreate(CreateView):
	model = Candidato
	form_class = Candidato_form
	template_name = 'candidato/candidato_form.html'
	success_url = 'https://www.google.cl/'

class CandidatoUpdate(UpdateView):
	model = Candidato	
	form_class = Candidato_form
	template_name = 'candidato/candidato_form.html'
	success_url = 'https://www.google.cl/'

	def form_valid(self, form):
			# Save the form instance
		self.object = form.save()

			# Get the files from the form
		certificado_antecedentes_files = self.request.FILES.getlist('certificado_antecedentes')
		hoja_de_vida_conductor_files = self.request.FILES.getlist('hoja_de_vida_conductor')
		certificado_residencia_files = self.request.FILES.getlist('certificado_residencia')
		certificado_afiliacion_afp_files = self.request.FILES.getlist('certificado_afiliacion_afp')
		certificado_afiliacion_salud_files = self.request.FILES.getlist('certificado_afiliacion_salud')
		fotocopia_cedula_identidad_files = self.request.FILES.getlist('fotocopia_cedula_identidad')
		fotocopia_licencia_conducir_files = self.request.FILES.getlist('fotocopia_licencia_conducir')	
		curriculum_vitae_files = self.request.FILES.getlist('curriculum_vitae')
		ultimo_finiquito_files = self.request.FILES.getlist('ultimo_finiquito')
		documentacion_que_acredite_el_cargo_files = self.request.FILES.getlist('documentacion_que_acredite_el_cargo')
		certificado_estudios_files = self.request.FILES.getlist('certificado_estudios')
		certificado_titulo_files = self.request.FILES.getlist('certificado_titulo')
		credencial_resolucion_sns_sernageomin_files = self.request.FILES.getlist('credencial_resolucion_sns_sernageomin')
		examen_preocupacional_salud_files = self.request.FILES.getlist('examen_preocupacional_salud')
		examen_preocupacional_alcohol_drogas_files = self.request.FILES.getlist('examen_preocupacional_alcohol_drogas')
		examen_psicosensometrico_files = self.request.FILES.getlist('examen_psicosensometrico')
		certificado_sustancias_peligrosas_files = self.request.FILES.getlist('certificado_sustancias_peligrosas')
		certificacion_rigger_files = self.request.FILES.getlist('certificacion_rigger')
		certificacion_pluma_files = self.request.FILES.getlist('certificacion_pluma')
		certificacion_choferes_operadores_files = self.request.FILES.getlist('certificacion_choferes_operadores')
		situacion_militar_files = self.request.FILES.getlist('situacion_militar')
		declaracion_jurada_salud_files = self.request.FILES.getlist('declaracion_jurada_salud')
		odi_collahuasi_covid19_files = self.request.FILES.getlist('odi_collahuasi_covid19')
		reglamento_interno_excon_files = self.request.FILES.getlist('reglamento_interno_excon')
		ficha_bhp_emex_files = self.request.FILES.getlist('ficha_bhp_emex')
		odis_tortolas_files = self.request.FILES.getlist('odis_tortolas')
		reglamento_conduccion_recibo_tortolas_files = self.request.FILES.getlist('reglamento_conduccion_recibo_tortolas')
		reglamento_conduccion_tortolas_anexo1_files = self.request.FILES.getlist('reglamento_conduccion_tortolas_anexo1')
		solicitud_evaluacion_conduccion_tortolas_files = self.request.FILES.getlist('solicitud_evaluacion_conduccion_tortolas')
		odis_conduccion_qb2_files = self.request.FILES.getlist('odis_conduccion_qb2')
		registro_asistencia_induccion_qb2_files = self.request.FILES.getlist('registro_asistencia_induccion_qb2')
		solicitud_licencia_interna_qb2_files = self.request.FILES.getlist('solicitud_licencia_interna_qb2')
		toma_conocimiento_covid19_files = self.request.FILES.getlist('toma_conocimiento_covid19')
		odis_qb22_files = self.request.FILES.getlist('odis_qb22')
		
		

			# Save the files to the server
		for file in certificado_antecedentes_files:
			self.object.certificado_antecedentes.save(file.name, file)
		for file in hoja_de_vida_conductor_files:
			self.object.hoja_de_vida_conductor.save(file.name, file)
		for file in certificado_residencia_files:
			self.object.certificado_residencia.save(file.name, file)
		for file in certificado_afiliacion_afp_files:
			self.object.certificado_afiliacion_afp.save(file.name, file)
		for file in certificado_afiliacion_salud_files:
			self.object.certificado_afiliacion_salud.save(file.name, file)
		for file in fotocopia_cedula_identidad_files:
			self.object.fotocopia_cedula_identidad.save(file.name, file)
		for file in fotocopia_licencia_conducir_files:
			self.object.fotocopia_licencia_conducir.save(file.name, file)
		for file in curriculum_vitae_files:
			self.object.curriculum_vitae.save(file.name, file)
		for file in ultimo_finiquito_files:
			self.object.ultimo_finiquito.save(file.name, file)
		for file in documentacion_que_acredite_el_cargo_files:
			self.object.documentacion_que_acredite_el_cargo.save(file.name, file)
		for file in certificado_estudios_files:
			self.object.certificado_estudios.save(file.name, file)
		for file in certificado_titulo_files:
			self.object.certificado_titulo.save(file.name, file)
		for file in credencial_resolucion_sns_sernageomin_files:
			self.object.credencial_resolucion_sns_sernageomin.save(file.name, file)
		for file in examen_preocupacional_salud_files:
			self.object.examen_preocupacional_salud.save(file.name, file)
		for file in examen_preocupacional_alcohol_drogas_files:
			self.object.examen_preocupacional_alcohol_drogas.save(file.name, file)
		for file in examen_psicosensometrico_files:
			self.object.examen_psicosensometrico.save(file.name, file)
		for file in certificado_sustancias_peligrosas_files:
			self.object.certificado_sustancias_peligrosas.save(file.name, file)
		for file in certificacion_rigger_files:
			self.object.certificacion_rigger.save(file.name, file)
		for file in certificacion_pluma_files:
			self.object.certificacion_pluma.save(file.name, file)
		for file in certificacion_choferes_operadores_files:
			self.object.certificacion_choferes_operadores.save(file.name, file)
		for file in situacion_militar_files:
			self.object.situacion_militar.save(file.name, file)
		for file in declaracion_jurada_salud_files:
			self.object.declaracion_jurada_salud.save(file.name, file)
		for file in odi_collahuasi_covid19_files:
			self.object.odi_collahuasi_covid19.save(file.name, file)
		for file in reglamento_interno_excon_files:
			self.object.reglamento_interno_excon.save(file.name, file)
		for file in ficha_bhp_emex_files:
			self.object.ficha_bhp_emex.save(file.name, file)
		for file in odis_tortolas_files:
			self.object.odis_tortolas.save(file.name, file)
		for file in reglamento_conduccion_recibo_tortolas_files:
			self.object.reglamento_conduccion_recibo_tortolas.save(file.name, file)
		for file in reglamento_conduccion_tortolas_anexo1_files:
			self.object.reglamento_conduccion_tortolas_anexo1.save(file.name, file)
		for file in solicitud_evaluacion_conduccion_tortolas_files:
			self.object.solicitud_evaluacion_conduccion_tortolas.save(file.name, file)
		for file in odis_conduccion_qb2_files:
			self.object.odis_conduccion_qb2.save(file.name, file)
		for file in registro_asistencia_induccion_qb2_files:
			self.object.registro_asistencia_induccion_qb2.save(file.name, file)
		for file in solicitud_licencia_interna_qb2_files:
			self.object.solicitud_licencia_interna_qb2.save(file.name, file)
		for file in toma_conocimiento_covid19_files:
			self.object.toma_conocimiento_covid19.save(file.name, file)
		for file in odis_qb22_files:
			self.object.odis_qb22.save(file.name, file)
		

			# Return the response
		return super().form_valid(form)
