# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0013_auto_20160709_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezervasyontalepler',
            name='r_isletme_brans',
            field=models.CharField(null=True, verbose_name='Branş', max_length=255),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(verbose_name='Kayıt Tarihi', max_length=100, default=datetime.datetime(2016, 7, 10, 0, 6, 57, 114467)),
        ),
    ]
