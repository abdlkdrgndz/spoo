# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0015_auto_20160710_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitap',
            name='yazar',
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 10, 1, 53, 52, 630725), verbose_name='Kayıt Tarihi', max_length=100),
        ),
        migrations.DeleteModel(
            name='Kitap',
        ),
        migrations.DeleteModel(
            name='Yazar',
        ),
    ]
