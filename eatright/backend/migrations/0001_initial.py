# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, default=3.0, max_digits=2)),
                ('distance', models.DecimalField(decimal_places=1, default=0.0, max_digits=4)),
            ],
        ),
    ]
