# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Framework(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/courses", blank=True, null=True)
    description = HTMLField()

    def __unicode__(self):
        return self.title


class Language(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/courses/languages", blank=True, null=True)
    framework = models.ForeignKey(Framework, related_name='languages')
    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=255)
    language = models.ForeignKey(Language, related_name='modules')
    price = models.PositiveIntegerField()
    content = HTMLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    enrolled_users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title
