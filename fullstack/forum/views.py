# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from models import Subject, Thread, Post


# Create your views here.
def forum(request):
    return render(request, 'forum/forum.html', {'subjects': Subject.objects.all()})


def threads(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'forum/threads.html', {'subject': subject})


