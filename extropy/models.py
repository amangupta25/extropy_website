# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
	contact = models.IntegerField(null=True)
	#Year_of_study = models.
	email = models.EmailField(null=True)



	def __str__(self):
		return self.name




