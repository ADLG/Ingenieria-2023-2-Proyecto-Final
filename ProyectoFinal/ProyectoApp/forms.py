from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class AgregaNombre(forms.Form):
	nombre = forms.CharField(label='Ingresa tu nombre', max_length=10)

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

class FormTickets(forms.ModelForm):
	class Meta:
		model = Tickets
		fields = ['id_ticket', "nombre", "precio", "cantidad"]
		labels = {
			'id_ticket': 'id_ticket',
			'nombre': 'nombre',
			'precio': 'precio',
			'cantidad': 'cantidad',
		}