# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-13 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='summary',
            field=models.CharField(max_length=100),
        ),
    ]
