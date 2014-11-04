# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20, blank=True)),
                ('password', models.CharField(max_length=40)),
                ('email_id', models.EmailField(unique=True, max_length=40)),
                ('age', models.IntegerField(default=None)),
                ('gender', models.CharField(max_length=10)),
                ('phone_num', models.CharField(max_length=10, blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'static/profile_images', blank=True)),
                ('date', models.DateTimeField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
