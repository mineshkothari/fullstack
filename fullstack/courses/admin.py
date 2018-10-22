# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Framework, Language, Module


# Register your models here.
admin.site.register(Framework)
admin.site.register(Language)
admin.site.register(Module)
