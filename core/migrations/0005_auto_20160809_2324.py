# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 23:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160809_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='publication_begin',
            new_name='begin_date',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='publication_creation',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='publication_end',
            new_name='end_date',
        ),
    ]
