# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-19 06:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_names'),
    ]

    operations = [
        migrations.DeleteModel(
            name='names',
        ),
    ]
