# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bakery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item')),
                ('name', models.CharField(max_length=250)),
                ('ingredients', models.TextField(max_length=1000)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item')),
                ('name', models.CharField(max_length=250)),
                ('ingredients', models.TextField(max_length=1000)),
                ('price', models.FloatField()),
            ],
        ),
    ]
