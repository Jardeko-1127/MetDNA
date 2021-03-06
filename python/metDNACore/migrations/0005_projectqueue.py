# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-23 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('metDNACore', '0004_auto_20171019_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=1)),
                ('paras', models.TextField(blank=True, default='', null=True)),
                ('status', models.CharField(default='done', max_length=10)),
                ('submit_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='queue', to='metDNACore.Project', verbose_name='project')),
            ],
        ),
    ]
