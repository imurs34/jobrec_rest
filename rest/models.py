from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
	title = models.CharField(max_length=250, default='')
	link = models.CharField(max_length=250, default='')
	category = models.CharField(max_length=250, default='')
