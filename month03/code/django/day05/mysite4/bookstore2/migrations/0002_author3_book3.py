# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-16 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='作者名称')),
            ],
        ),
        migrations.CreateModel(
            name='Book3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='书名')),
                ('authors', models.ManyToManyField(to='bookstore2.Author3')),
            ],
        ),
    ]
