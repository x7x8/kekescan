# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-30 03:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160627_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icpcheck',
            name='insert_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 30, 11, 31, 58, 18877), null=True),
        ),
        migrations.AlterField(
            model_name='subdomainbrute',
            name='fuzz_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 30, 11, 31, 58, 19476), null=True),
        ),
    ]