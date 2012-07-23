# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template 
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from plantilla.models import *
from plantilla.forms import *

#def lista_medicos(request):
	#medicos = Tbl1LlcMed.objects.all()
	#return render_to_response('lista_medicos.html',{'lista':medicos})


#formulario

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = "index.html"
    
    if request.method == 'POST':
        form = ElementoForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ElementoForm()
    data = {'form': form}
    return render_to_response(template, context_instance=RequestContext(request,data))