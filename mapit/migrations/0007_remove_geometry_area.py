# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-11 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapit', '0006_move_geometry_area_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geometry',
            name='area',
        ),
    ]