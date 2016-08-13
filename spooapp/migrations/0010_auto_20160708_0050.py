# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0009_auto_20160708_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezervasyontalepler',
            name='r_onay_durumu',
            field=models.CharField(choices=[('O', 'Onay'), ('R', 'Ret'), ('B', 'Beklemede')], verbose_name='Rezervasyon Onayı', max_length=255, help_text='Rezervasyon talebi onay/ret'),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 8, 0, 50, 36, 658417), verbose_name='Kayıt Tarihi', max_length=100),
        ),
    ]
