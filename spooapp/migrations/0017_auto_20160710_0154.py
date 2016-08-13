# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0016_auto_20160710_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(verbose_name='Kayıt Tarihi', default=datetime.datetime(2016, 7, 10, 1, 54, 14, 854336), max_length=100),
        ),
    ]
