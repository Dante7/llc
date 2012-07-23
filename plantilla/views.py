# Create your views here.
from plantilla.models import *
from django.shortcuts import render_to_response

def lista_medicos(request):
	medicos = Tbl1LlcMed.objects.all()
	return render_to_response('lista_medicos.html',{'lista':medicos})