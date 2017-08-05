# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
categories = (
    ('select', 'SELECT'),
    ('W', 'WORKSHOP'),
    ('M', 'MECHANIC'),
)
cities = (
    ('select', 'SELECT'),
    ('B', 'Banglore'),
    ('H', 'Hyderabad'),
)
class PartnersDetails(models.Model):
 name = models.CharField(max_length=20)
 address = models.CharField(max_length=80)
 type = models.CharField(max_length=20,choices=categories,default='select')
 city = models.CharField(max_length=20,choices=cities,default='select')
 code = models.CharField(primary_key=True,max_length=20)
 
 def __str__(self):
    return self.name
	
	
	
class ContactDetails(models.Model):
 wname = models.OneToOneField(PartnersDetails, on_delete=models.CASCADE)
 contact_number1=models.CharField(max_length=15,blank=False)
 contact_number2=models.CharField(max_length=15)
 
 def __str__(self):
    return "%s"% self.id
	
	
class Venue(models.Model):

    name = models.CharField(max_length=255)

    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
 
	
 
		
 