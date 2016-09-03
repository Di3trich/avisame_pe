# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160809_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=16, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=16, null=True)),
                ('altitude', models.DecimalField(blank=True, decimal_places=10, max_digits=16, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='publication',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Place'),
        ),
    ]