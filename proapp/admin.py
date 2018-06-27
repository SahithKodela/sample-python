# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Profile,EmployeeProfile, Employee,Text
admin.site.register(Profile)
admin.site.register(EmployeeProfile)
admin.site.register(Employee)
admin.site.register(Text)
#admin.site.register(LogOut)

# Register your models here.
