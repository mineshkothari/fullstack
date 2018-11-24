# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from models import Language, Module
from forms import NewLanguageForm, NewModuleForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf


def courses(request):
    return render(request, 'courses/languages.html', {'languages': Language.objects.all()})


def modules(request, language_id):
    language = get_object_or_404(Language, pk=language_id)
    return render(request, 'courses/modules.html', {'language': language})


def module_item(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    return render(request, 'courses/module_item.html', {'module': module})


def new_module(request):
    form = NewModuleForm
    return render(request, 'courses/new_module.html', {'form': form})


def new_language(request):
    form = NewLanguageForm
    return render(request, 'courses/new_language.html', {'form': form})
