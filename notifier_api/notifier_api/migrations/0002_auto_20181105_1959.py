# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifier_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationusers',
            name='notification_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='notifier_api.Notifications'),
        ),
    ]