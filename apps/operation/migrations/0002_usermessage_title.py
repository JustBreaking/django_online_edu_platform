# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-26 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='title',
            field=models.CharField(default='\u66ae\u96ea\u5728\u7ebf', max_length=32, verbose_name='\u6807\u9898'),
        ),
    ]
