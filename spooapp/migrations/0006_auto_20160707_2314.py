# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0005_auto_20160707_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_brans',
            field=models.ManyToManyField(max_length=255, verbose_name='İşletme Branşı', to='spooapp.SporDallar'),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 7, 23, 14, 22, 977677), max_length=100, verbose_name='Kayıt Tarihi'),
        ),
    ]
