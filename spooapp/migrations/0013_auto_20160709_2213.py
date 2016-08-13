# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0012_auto_20160709_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_hizmet_bedeli',
            field=models.DecimalField(help_text='Bir organizasyonun tam bedelini girin.', default='10.5', decimal_places=2, max_digits=300, verbose_name='Rezervasyon Bedeli'),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 9, 22, 13, 50, 929903), max_length=100, verbose_name='Kayıt Tarihi'),
        ),
    ]
