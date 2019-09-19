# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-19 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestampOfExpense', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('currency', models.CharField(choices=[('CAD', 'CAD'), ('HKD', 'HKD'), ('LVL', 'LVL'), ('PHP', 'PHP'), ('DKK', 'DKK'), ('HUF', 'HUF'), ('CZK', 'CZK'), ('AUD', 'AUD'), ('RON', 'RON'), ('SEK', 'SEK'), ('IDR', 'IDR'), ('INR', 'INR'), ('BRL', 'BRL'), ('RUB', 'RUB'), ('LTL', 'LTL'), ('JPY', 'JPY'), ('THB', 'THB'), ('CHF', 'CHF'), ('SGD', 'SGD'), ('PLN', 'PLN'), ('BGN', 'BGN'), ('TRY', 'TRY'), ('CNY', 'CNY'), ('NOK', 'NOK'), ('NZD', 'NZD'), ('ZAR', 'ZAR'), ('USD', 'USD'), ('MXN', 'MXN'), ('EEK', 'EEK'), ('GBP', 'GBP'), ('KRW', 'KRW'), ('MYR', 'MYR'), ('HRK', 'HRK')], max_length=3)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('clientname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientexpense.Client')),
            ],
        ),
    ]
