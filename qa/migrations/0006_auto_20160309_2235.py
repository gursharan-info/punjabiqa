# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_remove_dictionary_comprehension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='Word',
            field=models.CharField(default='adasd', max_length=200, unique=True, verbose_name='word'),
            preserve_default=False,
        ),
    ]
