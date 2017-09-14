# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-06 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170903_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Completed', 'Completed')], max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='thumbnail',
            field=models.ImageField(upload_to='polls/%Y/%m/%d'),
        ),
    ]
