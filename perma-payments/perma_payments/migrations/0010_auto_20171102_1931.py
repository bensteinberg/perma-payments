# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-02 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('perma_payments', '0009_auto_20170926_2053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalsubscriptionagreement',
            old_name='status_updated',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='subscriptionagreement',
            old_name='status_updated',
            new_name='updated_date',
        ),
        migrations.AddField(
            model_name='historicalsubscriptionagreement',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalsubscriptionagreement',
            name='paid_through',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscriptionagreement',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriptionagreement',
            name='paid_through',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
