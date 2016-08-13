# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0019_auto_20160710_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tesisler',
            name='isletme_hizmet_bedeli',
        ),
        migrations.RemoveField(
            model_name='tesisler',
            name='isletme_hizmet_kesinti_oran',
        ),
        migrations.RemoveField(
            model_name='tesisler',
            name='isletme_indirim_oran',
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 10, 17, 25, 47, 6152), max_length=100, verbose_name='Kayıt Tarihi'),
        ),
    ]
