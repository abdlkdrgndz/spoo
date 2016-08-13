# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0004_auto_20160707_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tesisler',
            name='isletme_hizmet_bitis',
        ),
        migrations.RemoveField(
            model_name='tesisler',
            name='isletme_hizmet_zaman',
        ),
        migrations.RemoveField(
            model_name='tesisler',
            name='isletme_brans',
        ),
        migrations.AddField(
            model_name='tesisler',
            name='isletme_brans',
            field=models.ManyToManyField(to='spooapp.SporDallar', max_length=255, verbose_name='İşletme Branşı', choices=[('FT', 'Futbol'), ('VB', 'Voleybol'), ('BT', 'Basketbol'), ('GK', 'Go-Kart'), ('TN', 'Tenis')]),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(max_length=100, verbose_name='Kayıt Tarihi', default=datetime.datetime(2016, 7, 7, 23, 5, 10, 371807)),
        ),
    ]
