# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Language(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/courses/languages", blank=True, null=True)
    description = HTMLField(blank=True)

    def __unicode__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=255)
    language = models.ForeignKey(Language, related_name='modules')
    description = HTMLField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    content = HTMLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    release_date = models.DateTimeField(blank=True, null=True)
    enrolled_users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title
