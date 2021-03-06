# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 02:05
from __future__ import unicode_literals

from django.db import migrations, models
import turtle_observer.models


class Migration(migrations.Migration):

    dependencies = [
        ('turtle_observer', '0003_expeditionlocation_expeditionobserver_observationobserver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='locationLat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='locationLong',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='ageInYears',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='bait',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='carapaceHeightCM',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='carapaceLengthCM',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='carapaceWidthCM',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='locationID',
            field=models.IntegerField(blank=True, null=True, verbose_name=turtle_observer.models.Location),
        ),
        migrations.AlterField(
            model_name='observation',
            name='massInGrams',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='observationNotes',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='plastronLengthCM',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='pondLocation',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='trapType',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='turtleID',
            field=models.IntegerField(blank=True, null=True, verbose_name=turtle_observer.models.Turtle),
        ),
        migrations.AlterField(
            model_name='turtle',
            name='turtleSex',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='turtle',
            name='turtleSpecies',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
