# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_favorite',
            field=models.BooleanField(default=False, verbose_name='Is favorite product?'),
        ),
    ]
