# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 19:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sending_dttm', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('status', models.CharField(max_length=16)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'email_service',
            },
        ),
    ]
