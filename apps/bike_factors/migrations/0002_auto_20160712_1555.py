# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_factors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cosmeticoption',
            options={'ordering': ['-price_factor']},
        ),
        migrations.AlterField(
            model_name='brandoption',
            name='requisites',
            field=models.ManyToManyField(to='bike_factors.BikeOption', verbose_name='Bike types that this feature is avalable for'),
        ),
        migrations.AlterField(
            model_name='cosmeticoption',
            name='requisites',
            field=models.ManyToManyField(to='bike_factors.BikeOption', verbose_name='Bike types that this feature is avalable for'),
        ),
        migrations.AlterField(
            model_name='featuresoption',
            name='requisites',
            field=models.ManyToManyField(to='bike_factors.BikeOption', verbose_name='Bike types that this feature is avalable for'),
        ),
        migrations.AlterField(
            model_name='frameoption',
            name='requisites',
            field=models.ManyToManyField(to='bike_factors.BikeOption', verbose_name='Bike types that this feature is avalable for'),
        ),
        migrations.AlterField(
            model_name='wheeloption',
            name='requisites',
            field=models.ManyToManyField(to='bike_factors.BikeOption', verbose_name='Bike types that this feature is avalable for'),
        ),
    ]