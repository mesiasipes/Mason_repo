# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.
class Picture(models.Model):
	created_date = models.DateTimeField(default=timezone.now)
	info = models.CharField(max_length=200)
	picture = models.ImageField(null=True)


	