# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_auto_20160309_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='Comprehension',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.Comprehension', verbose_name='Comprehension'),
        ),
    ]
