# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0020_auto_20160710_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tesisler',
            name='isletme_brans',
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(max_length=100, default=datetime.datetime(2016, 7, 10, 17, 27, 11, 768579), verbose_name='Kayıt Tarihi'),
        ),
    ]
