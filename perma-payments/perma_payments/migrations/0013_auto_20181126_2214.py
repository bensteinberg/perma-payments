# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-26 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perma_payments', '0012_auto_20180828_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeRequest',
            fields=[
                ('outgoingtransaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='perma_payments.OutgoingTransaction')),
                ('link_limit', models.CharField(help_text='For internal use only: link limit associated with the subscription', max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, help_text='Amount to be charged immediately', max_digits=19)),
                ('recurring_amount', models.DecimalField(decimal_places=2, help_text='Amount to be charged repeatedly, beginning on recurring_start_date', max_digits=19)),
                ('recurring_start_date', models.DateField(help_text='Date on which to commence charging recurring_amount')),
                ('recurring_frequency', models.CharField(choices=[('weekly', 'weekly'), ('bi-weekly', 'bi-weekly (every 2 weeks)'), ('quad-weekly', 'quad-weekly (every 4 weeks)'), ('monthly', 'monthly'), ('semi-monthly', 'semi-monthly (1st and 15th of each month)'), ('quarterly', 'quarterly'), ('semi-annually', 'semi-annually (twice every year)'), ('annually', 'annually')], max_length=20)),
                ('currency', models.CharField(default='USD', max_length=3)),
                ('locale', models.CharField(default='en-us', max_length=5)),
                ('payment_method', models.CharField(default='card', max_length=30)),
                ('transaction_type', models.CharField(default='sale,update_payment_token', max_length=30)),
                ('subscription_agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='change_requests', to='perma_payments.SubscriptionAgreement')),
            ],
            options={
                'abstract': False,
            },
            bases=('perma_payments.outgoingtransaction', models.Model),
        ),
        migrations.CreateModel(
            name='ChangeRequestResponse',
            fields=[
                ('response_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='perma_payments.Response')),
                ('related_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='change_request_response', to='perma_payments.ChangeRequest')),
            ],
            options={
                'abstract': False,
            },
            bases=('perma_payments.response',),
        ),
        migrations.AddField(
            model_name='subscriptionrequest',
            name='link_limit',
            field=models.CharField(default='unlimited', help_text='For internal use only: link limit associated with the subscription', max_length=20),
            preserve_default=False,
        ),
    ]