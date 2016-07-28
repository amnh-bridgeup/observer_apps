# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-28 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turtle_observer', '0011_remove_location_ordinal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turtle_observer.Location'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='observation_legacy_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
