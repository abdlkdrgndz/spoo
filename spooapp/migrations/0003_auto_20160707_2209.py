# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0002_auto_20160707_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesisler',
            name='isletme_hizmet_bitis',
            field=models.TimeField(null=True, verbose_name=' '),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 7, 22, 9, 9, 943577), max_length=100, verbose_name='Kayıt Tarihi'),
        ),
    ]
