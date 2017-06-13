# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from pictures.models import Picture

# Create your views here.
def pictures(request):
	context = {
		'pics': Picture.objects.all()
	}
	return render(request, 'pictures.html', context)