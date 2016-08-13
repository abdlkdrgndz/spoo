# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0003_auto_20160707_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_hizmet_bitis',
            field=models.DateTimeField(verbose_name='Seans Bitişi', null=True),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_hizmet_zaman',
            field=models.DateTimeField(verbose_name='Seans Başlangıcı', help_text='Rezervasyon saatlerinin başlangıç ve bitiş saatlerini belirleyin.'),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 7, 22, 18, 25, 945227), verbose_name='Kayıt Tarihi', max_length=100),
        ),
    ]
