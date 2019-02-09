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
    """
    Render list of available languages
    """
    languages = Language.objects.all().order_by('id')

    return render(request, 'courses/languages.html', {'languages': languages})


def modules(request, language_id):
    """
    Render list of released modules and filter them based on the language
    """
    language = get_object_or_404(Language, pk=language_id)
    selected_modules = language.modules.filter(
        release_date__lte=timezone.now()).order_by('-release_date')

    if request.user.is_authenticated:
        my_courses = list(request.user.module_set.all())
    else:
        my_courses = []

    args = {
        'my_courses': my_courses,
        'modules': selected_modules,
        'language': language,
    }

    return render(request, 'courses/modules.html', args)


@login_required(login_url='/account/login/')
def module_item(request, module_id):
    """
    Display module content
    """
    module = get_object_or_404(Module, pk=module_id)

    # If the user has purchased the module, display content
    if module in request.user.module_set.all():
        return render(request, 'courses/module_item.html', {'module': module})

    # If user has attempted to view content without a valid purchase, redirect to courses homepage
    else:
        return redirect(reverse('courses'))


@login_required(login_url='/account/login/')
def new_module(request):
    """
    Add a new module
    """
    # First check if user is Staff. If True and method is POST, add new module
    if request.user.is_staff:
        if request.method == 'POST':
            form = NewModuleForm(request.POST)
            if form.is_valid():
                module = form.save(False)
                module.release_date = timezone.now()
                module.save()
                messages.success(request, "%s successfully created" % module.title)
                return redirect(module_item, module.pk)

        # If method is GET, render blank form
        else:
            form = NewModuleForm()
        return render(request, 'courses/new_module.html', {'form': form})

    # If user is not Staff, redirect to courses homepage
    else:
        return redirect(reverse('courses'))


@login_required(login_url='/account/login/')
def new_language(request):
    """
    Add a new language
    """
    # First check if user is Staff. If True and method is POST, add new language
    if request.user.is_staff:
        if request.method == 'POST':
            form = NewLanguageForm(request.POST, request.FILES)
            print form.data
            if form.is_valid():
                language = form.save()
                messages.success(request, "%s successfully created" % language.title)
                return redirect(reverse('courses'))

        # If method is GET, render blank form
        else:
            form = NewLanguageForm()
        return render(request, 'courses/new_language.html', {'form': form})

    # If user is not Staff, redirect to courses homepage
    else:
        return redirect(reverse('courses'))
