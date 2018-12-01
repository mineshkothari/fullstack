# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from courses.models import Language, Module
from django.contrib.auth import get_user_model

User = get_user_model()


class OrderItem(models.Model):
    module = models.OneToOneField(Module, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.module.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item = models.ManyToManyField(OrderItem)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_order_items(self):
        return self.item.all()

    def get_order_total(self):
        return sum([item.module.price for item in self.item.all()])

    def __unicode__(self):
        return '{0}-{1}'.format(self.id, self.user)
