# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0026_auto_20160710_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 10, 18, 19, 1, 796058), max_length=100, verbose_name='Kayıt Tarihi'),
        ),
    ]
