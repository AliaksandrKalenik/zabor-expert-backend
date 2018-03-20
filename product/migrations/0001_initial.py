# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1000, unique=True, verbose_name='Category title')),
                ('priority_order', models.IntegerField(default=1, verbose_name='Priority order')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to=product.models.category_dir_path, verbose_name='Image')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='product.Category', verbose_name='Parent Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('priority_order', models.IntegerField(default=1, verbose_name='Priority Order')),
                ('title', models.CharField(db_index=True, max_length=1000)),
                ('description', models.TextField()),
                ('long_description', models.TextField()),
                ('old_price', models.FloatField(blank=True, null=True, verbose_name='Old product price')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Product price')),
                ('price_units', models.CharField(default='руб./секция', max_length=100)),
                ('old_installation_price', models.FloatField(blank=True, null=True, verbose_name='Old installation product price')),
                ('installation_price', models.FloatField(blank=True, null=True, verbose_name='Installation product price')),
                ('installation_price_units', models.CharField(default='руб./секция', max_length=100)),
                ('old_premium_installation_price', models.FloatField(blank=True, null=True, verbose_name='Old premium installation product price')),
                ('premium_installation_price', models.FloatField(blank=True, null=True, verbose_name='Premium installation product price')),
                ('premium_installation_price_units', models.CharField(default='руб./секция', max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=product.models.product_image_dir_path, verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.Product', verbose_name='product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('priority_order', models.IntegerField(default=1, verbose_name='Priority order')),
                ('title', models.TextField(verbose_name='Title')),
                ('value', models.TextField(verbose_name='Value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='product.Product', verbose_name='Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]