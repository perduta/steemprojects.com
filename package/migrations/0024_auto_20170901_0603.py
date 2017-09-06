# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-01 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0023_timelineevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelineevent',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='package.Project'),
        ),
    ]