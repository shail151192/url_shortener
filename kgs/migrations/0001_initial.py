# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-13 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=6, unique=True)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
    ]
