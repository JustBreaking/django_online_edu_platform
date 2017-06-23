# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-22 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20170622_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to=b'org/%Y%m', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default=b'teacher/default.png', upload_to=b'teacher/%Y%m', verbose_name='\u5934\u50cf'),
        ),
    ]
