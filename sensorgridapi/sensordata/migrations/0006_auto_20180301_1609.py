# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensordata', '0005_sensordata_data_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=9, null=True),
        ),
    ]
