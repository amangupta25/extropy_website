# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from forms import RegisterForm

# Create your views here.

def index(request):
	return render(request, 'extropy/index.html')

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid: 
			form_object=form.save()
			return redirect(reverse('extropy:index'))
	else:
		form = RegisterForm()

	return render(request,'extropy/register-form.html',{'form': form })

	