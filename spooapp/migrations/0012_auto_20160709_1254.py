# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0011_auto_20160709_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='bransucretleri',
            name='isletme_adi',
            field=models.ForeignKey(null=True, verbose_name='Tesis Adı', to='spooapp.Tesisler'),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(max_length=100, verbose_name='Kayıt Tarihi', default=datetime.datetime(2016, 7, 9, 12, 54, 52, 966246)),
        ),
    ]
