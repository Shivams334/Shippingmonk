from __future__ import unicode_literals

from django.db import models

from django.core.validators import RegexValidator

# Create your models here.

class orderDetail(models.Model):
	Name = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now_add = True,auto_now=False)
	Address = models.CharField(max_length=200)
	orderId = models.CharField(max_length=200)


class shop(models.Model):
	hname = models.CharField(max_length=20)
	hubId = models.CharField(max_length=10)
	address = models.CharField(max_length=30)
	Auth_to = models.CharField(max_length=10)
	email = models.EmailField()
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True,max_length=12) #validators should be a list