# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-05-07 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledgerlink', '0018_vslacreditscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='vslacreditscore',
            name='DateProcessed',
            field=models.DateField(blank=True, null=True),
        ),
    ]