# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.validators import RegexValidator
# Create your models here.

class Event(models.Model):
	ename = models.CharField("Event Name",max_length=250)
	edate = models.DateTimeField("Date")

	def __str__(self):
		return self.ename


class Register(models.Model):
		
	GENDER_CHOICES = (
		('M','MALE'),
		('F','FEMALE')
	)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	name = models.CharField("Name",max_length=250)
	idno = models.CharField("Id No.",max_length=400)
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
	
	#contact_regex = RegexValidator(regex= r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
	#contact = models.CharField(validators=[contact_regex],max_length=10,null=True)
	contact = models.CharField(max_length=10,null=True)
	#Year_of_study = models.
	email = models.EmailField(null=True)

	def __str__(self):
		return self.name




