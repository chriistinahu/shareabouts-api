# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-29 16:58
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sa_api_v2', '0004_django_19_updates'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attachment',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
