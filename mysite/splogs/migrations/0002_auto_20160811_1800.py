# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-11 18:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='date',
            field=models.DateField(default=datetime.date(2016, 8, 11)),
        ),
    ]
