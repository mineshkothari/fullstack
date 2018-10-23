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
    return render(request, 'courses/frameworks.html', {'frameworks': Framework.objects.all()})


def languages(request, framework_id):
    framework = get_object_or_404(Framework, pk=framework_id)
    return render(request, 'courses/languages.html', {'framework': framework})
