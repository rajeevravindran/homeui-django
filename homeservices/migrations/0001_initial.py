# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-21 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AlarmName', models.CharField(help_text='Name of the Alarm', max_length=255)),
                ('AlarmTime', models.DateTimeField()),
                ('AlarmKilled', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
