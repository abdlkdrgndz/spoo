# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0022_auto_20160710_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(verbose_name='Kayıt Tarihi', default=datetime.datetime(2016, 7, 10, 17, 50, 39, 669772), max_length=100),
        ),
    ]
