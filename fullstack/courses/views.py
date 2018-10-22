# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from models import Framework, Language, Module
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf


# Create your views here.
def courses(request):
    return render(request, 'courses/courses.html', {'framework': Framework.objects.all()})
