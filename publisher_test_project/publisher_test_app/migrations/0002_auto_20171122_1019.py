# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 16:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher_test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publishertestmodel',
            options={'permissions': (('can_publish', 'Can publish'),), 'verbose_name': 'Publisher Test Model', 'verbose_name_plural': 'Publisher Test Model'},
        ),
    ]