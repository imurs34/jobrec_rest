from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
	title = models.CharField(max_length=250, default='')
	link = models.CharField(max_length=250, default='')
	category = models.CharField(max_length=250, default='')

class Ints(models.Model):
	ints1 = models.CharField(max_length=250, default='')
	ints2 = models.CharField(max_length=250, default='')

class User(models.Model):
	FirstName = models.CharField(max_length=250, default='')
	LastName = models.CharField(max_length=250, default='')
	Email = models.CharField(max_length=250, default='')

	interests = models.ForeignKey(
		Ints,
		default='',
		on_delete=models.CASCADE
	)
