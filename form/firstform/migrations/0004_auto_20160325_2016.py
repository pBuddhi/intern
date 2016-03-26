# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 14:46
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstform', '0003_enquiry_need'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseInsert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='invalid', regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200)),
                ('mehman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstform.DatabaseInsert')),
            ],
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='requirement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstform.Guest'),
        ),
    ]
