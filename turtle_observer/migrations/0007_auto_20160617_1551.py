# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turtle_observer', '0006_auto_20160617_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expeditionlocation',
            old_name='expedition_id',
            new_name='expedition',
        ),
        migrations.RenameField(
            model_name='expeditionlocation',
            old_name='location_id',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='expeditionobserver',
            old_name='expedition_id',
            new_name='expedition',
        ),
        migrations.RenameField(
            model_name='expeditionobserver',
            old_name='observer_id',
            new_name='observer',
        ),
        migrations.RenameField(
            model_name='observation',
            old_name='expedition_id',
            new_name='expedition',
        ),
        migrations.RenameField(
            model_name='observationobserver',
            old_name='observation_id',
            new_name='observation',
        ),
        migrations.RenameField(
            model_name='observationobserver',
            old_name='observer_id',
            new_name='observer',
        ),
        migrations.AlterField(
            model_name='observation',
            name='location_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='turtle_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
