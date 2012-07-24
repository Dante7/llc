from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Tbl1LlcMed(models.Model):
    id_tbl1 = models.IntegerField(primary_key=True)
    folio = models.IntegerField()
    nombre_medico = models.CharField(max_length=800)
    institucion = models.CharField(max_length=45)
    hospital = models.CharField(max_length=750)
    cod_med = models.CharField(max_length=21)
    fecha_llenado = models.DateField()
    class Meta:
        db_table = u'tbl1_llc_med'

class Tbl2LlcPaciente(models.Model):
    id_tbl2 = models.IntegerField(primary_key=True)
    tbl1 = models.ForeignKey(Tbl1LlcMed)
    cup = models.CharField(max_length=9)
    edad = models.IntegerField()
    peso = models.IntegerField()
    talla = models.IntegerField()
    superficie_corporal = models.IntegerField()
    sexo = models.CharField(max_length=18)
    asegurado = models.CharField(max_length=6)
    aseguradora = models.CharField(max_length=150, blank=True)
    paciente = models.CharField(max_length=90, blank=True)
    tipo_paciente = models.CharField(max_length=120, blank=True)
    pac_30_dias = models.IntegerField(null=True, blank=True)
    pac_diag_llc = models.IntegerField(null=True, blank=True)
    pac_ver_esperar = models.IntegerField(null=True, blank=True)
    pac_tx = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tbl2_llc_paciente'

class Tbl3LlcHistorial(models.Model):
    id_tbl3 = models.IntegerField(primary_key=True)
    tbl1 = models.ForeignKey(Tbl1LlcMed)
    ocupacion = models.CharField(max_length=150, blank=True)
    det_ninguno = models.IntegerField(null=True, blank=True)
    det_anemia = models.IntegerField(null=True, blank=True)
    det_sintomas_b = models.IntegerField(null=True, blank=True)
    det_infeccion = models.IntegerField(null=True, blank=True)
    det_tumor = models.IntegerField(null=True, blank=True)
    det_adenomegalias = models.IntegerField(null=True, blank=True)
    det_dolor = models.IntegerField(null=True, blank=True)
    det_otros = models.CharField(max_length=450, blank=True)
    class Meta:
        db_table = u'tbl3_llc_historial'

class Tbl4LlcRuta(models.Model):
    id_tbl4 = models.IntegerField(primary_key=True)
    tbl3 = models.ForeignKey(Tbl3LlcHistorial)
    n_ruta = models.IntegerField(null=True, blank=True)
    especialidad = models.CharField(max_length=135, blank=True)
    institucion = models.CharField(max_length=60, blank=True)
    tiempo_a = models.IntegerField(null=True, blank=True)
    tiempo_m = models.IntegerField(null=True, blank=True)
    tiempo_s = models.IntegerField(null=True, blank=True)
    diagnostico = models.CharField(max_length=180, blank=True)
    recibio_tx = models.CharField(max_length=6, blank=True)
    class Meta:
        db_table = u'tbl4_llc_ruta'

class Tbl5LlcDxCancer(models.Model):
    id_tbl5 = models.IntegerField(primary_key=True)
    tbl1 = models.ForeignKey(Tbl1LlcMed)
    eg_ninguno = models.IntegerField(null=True, blank=True)
    eg_ldh = models.IntegerField(null=True, blank=True)
    eg_microglobulina = models.IntegerField(null=True, blank=True)
    eg_electro_proteinas = models.IntegerField(null=True, blank=True)
    eg_inmunoglobulinas = models.IntegerField(null=True, blank=True)
    eg_coombs_directo = models.IntegerField(null=True, blank=True)
    eg_rx_torax = models.IntegerField(null=True, blank=True)
    eg_ultra_abdomen = models.IntegerField(null=True, blank=True)
    eg_tomo_axial = models.IntegerField(null=True, blank=True)
    eg_aspirado_biopsia = models.IntegerField(null=True, blank=True)
    eg_fish = models.IntegerField(null=True, blank=True)
    eg_frotis = models.IntegerField(null=True, blank=True)
    eg_sanguineo = models.IntegerField(null=True, blank=True)
    eg_pcr = models.IntegerField(null=True, blank=True)
    eg_cariotipo = models.IntegerField(null=True, blank=True)
    eg_otros = models.IntegerField(null=True, blank=True)
    estadio = models.CharField(max_length=9, blank=True)
    subetapa = models.CharField(max_length=3, blank=True)
    ver_esperar = models.CharField(max_length=6, blank=True)
    duracion_m = models.IntegerField(null=True, blank=True)
    duracion_a = models.IntegerField(null=True, blank=True)
    linfo_dx = models.IntegerField(null=True, blank=True)
    linfo_30_d = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tbl5_llc_dx_cancer'

class Tbl6LlcFactores(models.Model):
    id_tbl6 = models.IntegerField(primary_key=True)
    tbl1 = models.ForeignKey(Tbl1LlcMed)
    ecog = models.CharField(max_length=150, blank=True)
    fact_ninguno = models.IntegerField(null=True, blank=True)
    fact_17p = models.IntegerField(null=True, blank=True)
    fact_13q = models.IntegerField(null=True, blank=True)
    fact_12 = models.IntegerField(null=True, blank=True)
    fact_11q = models.IntegerField(null=True, blank=True)
    fact_zap70 = models.IntegerField(null=True, blank=True)
    fact_mutacion_lgvh = models.IntegerField(null=True, blank=True)
    fact_microglobulina = models.IntegerField(null=True, blank=True)
    fact_otros = models.IntegerField(null=True, blank=True)
    fact_otros_espe = models.CharField(max_length=450, blank=True)
    marc_cd38 = models.IntegerField(null=True, blank=True)
    marc_cd11c = models.IntegerField(null=True, blank=True)
    marc_cd20 = models.IntegerField(null=True, blank=True)
    marc_cd21 = models.IntegerField(null=True, blank=True)
    marc_cd22 = models.IntegerField(null=True, blank=True)
    marc_cd23 = models.IntegerField(null=True, blank=True)
    marc_cd25 = models.IntegerField(null=True, blank=True)
    marc_cd5 = models.IntegerField(null=True, blank=True)
    marc_hla_dr = models.IntegerField(null=True, blank=True)
    marc_smlg = models.IntegerField(null=True, blank=True)
    marc_otros = models.IntegerField(null=True, blank=True)
    marc_otros_res = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = u'tbl6_llc_factores'

class Tbl7LlcTratamiento(models.Model):
    id_tbl7 = models.IntegerField(primary_key=True)
    tbl1 = models.ForeignKey(Tbl1LlcMed)
    tx_vigilancia = models.IntegerField(null=True, blank=True)
    tx_qx = models.IntegerField(null=True, blank=True)
    tx_esplectomia = models.IntegerField(null=True, blank=True)
    tx_cel_madre = models.IntegerField(null=True, blank=True)
    tx_rx = models.IntegerField(null=True, blank=True)
    tx_inmuno_qx = models.IntegerField(null=True, blank=True)
    tx_otro = models.CharField(max_length=300, blank=True)
    etapa_actual = models.CharField(max_length=300, blank=True)
    respuesta_tx = models.CharField(max_length=300, blank=True)
    no_valorable = models.CharField(max_length=450, blank=True)
    comorb_ninguna = models.IntegerField(null=True, blank=True)
    comorb_vih = models.IntegerField(null=True, blank=True)
    comorb_ins_cardiaca = models.IntegerField(null=True, blank=True)
    comorb_epoc = models.IntegerField(null=True, blank=True)
    comorb_ins_renal = models.IntegerField(null=True, blank=True)
    comorb_disf_pulmonaria = models.IntegerField(null=True, blank=True)
    comorb_ictericia = models.IntegerField(null=True, blank=True)
    comorb_tromboembolismo = models.IntegerField(null=True, blank=True)
    comorb_coaugulopatia = models.IntegerField(null=True, blank=True)
    comorb_trans_gastro = models.IntegerField(null=True, blank=True)
    comorb_diabetes = models.IntegerField(null=True, blank=True)
    comorb_hipertension = models.IntegerField(null=True, blank=True)
    comorb_hepatitis = models.IntegerField(null=True, blank=True)
    comorb_otros = models.CharField(max_length=450, blank=True)
    class Meta:
        db_table = u'tbl7_llc_tratamiento'

class Tbl8LlcTxActual(models.Model):
    id_tbl8 = models.IntegerField(primary_key=True)
    tbl1 = models.ForeignKey(Tbl1LlcMed)
    tipo_tx = models.CharField(max_length=60, blank=True)
    producto = models.CharField(max_length=150, blank=True)
    principio = models.CharField(max_length=150, blank=True)
    dosis_aplicada = models.IntegerField(null=True, blank=True)
    dosis_dia = models.IntegerField(null=True, blank=True)
    dosis_dia_unidad = models.CharField(max_length=15, blank=True)
    veces_aplicado = models.IntegerField(null=True, blank=True)
    dias_aplica_ini = models.IntegerField(null=True, blank=True)
    dias_aplica_fin = models.IntegerField(null=True, blank=True)
    duracion_ciclos = models.IntegerField(null=True, blank=True)
    ciclos_aplicados = models.IntegerField(null=True, blank=True)
    ciclos_planeados = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tbl8_llc_tx_actual'

class Tbl9LlcTxPrevio(models.Model):
    id_tbl9 = models.IntegerField(primary_key=True)
    tbl1 = models.ForeignKey(Tbl1LlcMed)
    tx_previo = models.CharField(max_length=6, blank=True)
    respondio_tx = models.CharField(max_length=6, blank=True)
    tlp_a = models.IntegerField(null=True, blank=True)
    tlp_m = models.IntegerField(null=True, blank=True)
    qx_citotoxica = models.CharField(max_length=90, blank=True)
    anticuerpo_monoclonal = models.CharField(max_length=6, blank=True)
    otros = models.CharField(max_length=300, blank=True)
    terapia_soporte = models.CharField(max_length=6, blank=True)
    ms_analgesico_aine = models.IntegerField(null=True, blank=True)
    ms_analgesico_opioide = models.IntegerField(null=True, blank=True)
    ms_diuretico = models.IntegerField(null=True, blank=True)
    ms_antiemetico = models.IntegerField(null=True, blank=True)
    ms_antihipertensivo = models.IntegerField(null=True, blank=True)
    ms_anticoagulante = models.IntegerField(null=True, blank=True)
    ms_fec = models.IntegerField(null=True, blank=True)
    ms_tx_inc_plaquetas = models.IntegerField(null=True, blank=True)
    ea_ninguno = models.IntegerField(null=True, blank=True)
    ea_anemia = models.IntegerField(null=True, blank=True)
    ea_diarrea = models.IntegerField(null=True, blank=True)
    ea_nausea = models.IntegerField(null=True, blank=True)
    ea_dolor = models.IntegerField(null=True, blank=True)
    ea_fiebre = models.IntegerField(null=True, blank=True)
    ea_rash = models.IntegerField(null=True, blank=True)
    ea_cambios_ta = models.IntegerField(null=True, blank=True)
    ea_dist_abdominal = models.IntegerField(null=True, blank=True)
    ea_cambios_fc = models.IntegerField(null=True, blank=True)
    ea_trombositopenia = models.IntegerField(null=True, blank=True)
    ea_vomito = models.IntegerField(null=True, blank=True)
    ea_neutropenia = models.IntegerField(null=True, blank=True)
    ea_otros = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tbl9_llc_tx_previo'

class Tbl10LlcLineasPrevias(models.Model):
    id_tbl10 = models.IntegerField(primary_key=True)
    tbl1 = models.ForeignKey(Tbl1LlcMed)
    linea_previa = models.CharField(max_length=60, blank=True)
    duracion = models.IntegerField(null=True, blank=True)
    respondedor_a = models.IntegerField(null=True, blank=True)
    respondedor_m = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tbl10_llc_lineas_previas'

class Tbl11LlcEsqPrevio(models.Model):
    id_tbl11 = models.IntegerField(primary_key=True)
    tbl8_db = models.ForeignKey(Tbl10LlcLineasPrevias, db_column='tbl8_db')
    producto = models.CharField(max_length=90, blank=True)
    principio = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'tbl11_llc_esq_previo'

