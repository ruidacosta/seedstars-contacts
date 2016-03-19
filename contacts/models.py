from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=100, primary_key=True)
