# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lupsEdgeServer', '0002_auto_20160528_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='cron',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='interval',
            field=models.TextField(null=True),
        ),
    ]
