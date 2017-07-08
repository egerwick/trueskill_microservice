# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-22 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_greeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(blank=True, default=b'', max_length=100)),
                ('players', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Player')),
            ],
        ),
    ]