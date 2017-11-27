# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=120)
    branch = models.CharField(max_length=120)
    description = models.CharField(max_length=120)


class OperatingHours(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    open_hour = models.TimeField()
    close_hour = models.TimeField()
