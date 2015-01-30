from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm
from django import forms
from gestionEquipos.models import Equipo, Jugador
from django.contrib.auth.models import User


class EquipoForm(ModelForm):
	class Meta:
		model=Equipo
		fields = '__all__'
		#exclude = ['user', 'bottles']
		#fields = ['user', 'bottles']
	 #def __init__(self, *args, **kwargs):
		#super(EquipoForm, self).__init__(*args, **kwargs)

class JugadorForm(ModelForm):
	class Meta:
		model=Jugador
		fields = '__all__'

		
		


