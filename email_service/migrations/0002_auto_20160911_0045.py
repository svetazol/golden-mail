# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 00:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('email_service', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailService',
            new_name='EmailRequest',
        ),
        migrations.AlterModelTable(
            name='emailrequest',
            table='email_request',
        ),
    ]
