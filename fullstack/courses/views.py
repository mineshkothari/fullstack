# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
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


@login_required
def new_module(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            form = NewModuleForm(request.POST)
            if form.is_valid():
                module = form.save(False)
                module.release_date = timezone.now()
                module.save()
                messages.success(request, "New module successfully added")
                return redirect(module_item, module.pk)
        else:
            form = NewModuleForm
            return render(request, 'courses/new_module.html', {'form': form})
    else:
        return redirect(reverse('courses'))


# def new_module(request, language_id):
#     language = get_object_or_404(Language, pk=language_id)
#
#     if request.user.is_authenticated and request.user.is_staff:
#         if request.method == 'POST':
#             form = NewModuleForm(request.POST)
#             if form.is_valid():
#                 module = form.save(False)
#                 module.language = language
#                 module.release_date = timezone.now()
#                 module.save()
#                 messages.success(request, "New module successfully added")
#                 return redirect(module_item, language.pk)
#         else:
#             form = NewModuleForm
#             return render(request, 'courses/new_module.html', {'form': form})
#     else:
#         return redirect(reverse('courses'))

@login_required
def new_language(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            form = NewLanguageForm(request.POST)
            if form.is_valid():
                language = form.save(False)
                language.release_date = timezone.now()
                language.save()
                messages.success(request, "New language successfully created")
                return redirect(module_item, language.pk)
        else:
            form = NewLanguageForm
            return render(request, 'courses/new_language.html', {'form': form})
    else:
        return redirect(reverse('courses'))
