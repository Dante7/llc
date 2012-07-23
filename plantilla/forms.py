#encoding:utf-8
from django.forms import ModelForm
from django import forms
from plantilla.models import *

class pc(forms.Form):
	"""docstring for pc"""
	
	def __init__(self, arg):
		super(pc, self).__init__()
		self.arg = arg
