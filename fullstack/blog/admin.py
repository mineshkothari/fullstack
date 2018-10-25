# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from . models import Post
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


# admin.site.register(Post)
admin.site.register(Post, SomeModelAdmin)

