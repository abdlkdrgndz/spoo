# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0018_auto_20160710_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(max_length=100, default=datetime.datetime(2016, 7, 10, 14, 24, 54, 70408), verbose_name='Kayıt Tarihi'),
        ),
    ]
