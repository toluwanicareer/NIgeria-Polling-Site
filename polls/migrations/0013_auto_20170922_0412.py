# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_choice_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
