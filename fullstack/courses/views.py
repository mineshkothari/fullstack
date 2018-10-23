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
    return render(request, 'courses/courses.html', {'frameworks': Framework.objects.all()})


# def frameworks(request, framework_title):
#     framework_ = get_object_or_404(Framework, title=framework_title)
#     return render(request, 'courses/frameworks.html', {'framework': framework_})

def frameworks(request, framework_id):
    framework_ = get_object_or_404(Framework, pk=framework_id)
    return render(request, 'courses/frameworks.html', {'framework': framework_})


# def language(request, language_id):
#     language_ = get_object_or_404(Language, pk=language_id)
#     args = {'language': language_}
#     args.update(csrf(request))
#     return render(request, 'courses/language.html', args)
