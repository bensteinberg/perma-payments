# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-17 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('perma_payments', '0008_auto_20170816_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutgoingTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_perma_payments.outgoingtransaction_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
