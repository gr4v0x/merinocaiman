# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0003_auto_20170209_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteBook',
            fields=[
                ('note', models.CharField(max_length=20000)),
                ('dateTimeAdded', models.DateTimeField(auto_now_add=True)),
                ('noteKey', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
        ),
    ]
