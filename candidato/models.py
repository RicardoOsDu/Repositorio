from django.db import models
import os
from uuid import uuid4



# Create your models here.

#def directorio_candidato(instance, filename):
#    upload_to = '/candidatos/'
 #   ext = filename.split('.')[-1]
  #  # get filename
  #  if instance:
   #     filename = '{}.{}'.format(instance, ext)
#    else:
        # set filename as random string
 #       filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
 #   return os.path.join(upload_to, filename)

cc= (
        ('1','Quebrada Blanca'),
        ('2','Lo Pinto'),
        ('3','Oficina Central'),
        ('4','Carbonato'),
        ('5','Toconao'),
        ('6','Centinela'),
        ('7','Spence'),
        ('8','La Negra'),
    )

def upload_directory_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "DSR_%s_%s_0.%s" % (instance.rut, instance.nombre , ext)
    return os.path.join('uploads',filename)

class Candidato(models.Model):
    nombre = models.CharField(max_length = 70, null=True, blank=True)
    rut = models.CharField(max_length = 10, primary_key=True)
    correo = models.EmailField(null=True, blank=True)
    centro_de_costo =models.CharField(null=True, blank=True, max_length =30, choices = cc)
    estado = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(upload_to=upload_directory_name, null=True, blank=True)
    certificado_antecedentes = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    hoja_de_vida_conductor = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    certificado_residencia = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    certificado_afiliacion_afp = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    certificado_afiliacion_salud = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    fotocopia_cedula_identidad = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    fotocopia_licencia_conducir = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    curriculum_vitae = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    ultimo_finiquito = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    documentacion_que_acredite_el_cargo = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    certificado_estudios = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    certificado_titulo = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    credencial_resolucion_sns_sernageomin = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    examen_preocupacional_salud = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    examen_preocupacional_alcohol_drogas = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    examen_psicosensometrico = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    certificado_sustancias_peligrosas = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    certificacion_rigger = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    certificacion_pluma = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    certificacion_choferes_operadores = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    situacion_militar = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    declaracion_jurada_salud = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    odi_collahuasi_covid19 = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    reglamento_interno_excon = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    ficha_bhp_emex = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    odis_tortolas = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    reglamento_conduccion_recibo_tortolas = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    reglamento_condiccion_tortolas_anexo1 = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    solicitud_evaluacion_conduccion_tortolas = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    odis_conduccion_qb2 = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    registro_asistencia_induccion_qb2 = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    solicitud_licencia_interna_qb2 = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    toma_conocimiento_covid19 = models.FileField(upload_to=upload_directory_name, null=True, blank=True)
    odis_qb22 = models.FileField(upload_to=upload_directory_name, null=True, blank=True)

    
    class Meta:
        verbose_name="candidato"
        verbose_name_plural="candidatos"

    def __str__(self):
        return self.nombre +" "+ self.rut
      
"""
class Centro_de_costo(models.Model):
    nombre = models.CharField(max_length = 70, null=True, blank=True)
    id_cc = models.IntegerField()
"""