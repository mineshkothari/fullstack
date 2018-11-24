# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Language, Module
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


# Register your models here.
admin.site.register(Language, SomeModelAdmin)
admin.site.register(Module, SomeModelAdmin)
