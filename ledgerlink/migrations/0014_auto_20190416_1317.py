# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-16 10:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledgerlink', '0013_auto_20190403_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanissue',
            old_name='InterestAmout',
            new_name='InterestAmount',
        ),
    ]
