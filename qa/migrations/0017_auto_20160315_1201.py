# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0016_auto_20160314_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='NamedEntity',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='AnswerRemarks',
            field=models.CharField(blank=True, max_length=500, verbose_name='Remarks'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='AnswerTypeID',
            field=models.ManyToManyField(blank=True, to='qa.AnswerType', verbose_name='Answer Type'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='LexicalDensity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ReadabilityIndex',
            field=models.FloatField(),
        ),
    ]
