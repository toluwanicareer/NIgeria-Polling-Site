# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-03 04:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170903_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='user_choice',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
