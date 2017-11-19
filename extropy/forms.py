from django.contrib.auth.models import User
from models import *
from django import forms

class RegisterForm(forms.ModelForm):

	class Meta:
		model = Register
		fields = ['name','idno','gender','contact','email','event']

