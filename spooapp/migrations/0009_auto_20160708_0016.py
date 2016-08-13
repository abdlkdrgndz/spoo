# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0008_auto_20160708_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezervasyontalepler',
            name='r_isletme_adi',
            field=models.CharField(verbose_name='Rezervasyon Talebinde Bulunulan İşletme', max_length=255),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(verbose_name='Kayıt Tarihi', max_length=100, default=datetime.datetime(2016, 7, 8, 0, 16, 11, 981412)),
        ),
    ]
