# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-11 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0003_auto_20180611_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='to',
            field=models.CharField(max_length=150),
        ),
    ]
