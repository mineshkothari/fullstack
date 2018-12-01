# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from courses.models import Language, Module
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}-{1}'.format(self.id, self.user)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.module.title
