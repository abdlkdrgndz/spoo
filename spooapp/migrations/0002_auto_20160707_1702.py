# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesisler',
            name='isletme_hizmetleri',
            field=models.ManyToManyField(to='spooapp.Uniteler'),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 7, 17, 2, 57, 689460), verbose_name='Kayıt Tarihi', max_length=100),
        ),
    ]
