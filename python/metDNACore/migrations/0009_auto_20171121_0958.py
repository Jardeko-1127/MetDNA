# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metDNACore', '0008_auto_20171115_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='polarity',
            field=models.CharField(default='NEG', max_length=12),
        ),
    ]
