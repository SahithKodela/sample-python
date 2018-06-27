# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

user = settings.AUTH_USER_MODEL
class Name(models.Model):
    name = models.ForeignKey(user)


class Profile(models.Model):
    name = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    FatherName = models.CharField(max_length=250)
    DateofBirth = models.DateField(auto_now=False)
    age = models.IntegerField()
    address = models.CharField(max_length=450, default={})
    timestamp = models.DateTimeField(auto_now=True)
    image = models.FileField(null=True, blank=True)
    def __str__(self):
     return self.name

class EmployeeProfile(models.Model):
    name = models.ForeignKey(user)
    date = models.DateField(auto_now=True)
    login = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=500, default={})
    logout = models.DateTimeField(auto_now=True)

class Log(models.Model):
    name = models.ForeignKey(user)
    logout = models.DateTimeField(auto_now=True)

class Employee(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField(auto_now=False, auto_now_add=False)
    login = models.DateTimeField(auto_now=False, auto_now_add=False)
    logout = models.DateTimeField(auto_now=False,auto_now_add=False)

class Text(models.Model):
    name = models.ForeignKey(user)
    to = models.CharField(max_length=150)
    text = models.TextField(max_length=750)

# Create your models here.
