# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=120)
    branch = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
