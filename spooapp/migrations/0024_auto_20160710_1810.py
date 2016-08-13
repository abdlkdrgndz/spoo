# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0023_auto_20160710_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bransucretleri',
            name='brans_adi',
            field=models.CharField(max_length=255, choices=[('AT', 'Atıcılık'), ('HT', 'Hentbol'), ('BP', 'Buz Pateni'), ('VB', 'Voleybol'), ('TN', 'Tenis'), ('PB', 'Paintball'), ('MT', 'Masa Tenisi'), ('KA', 'Kayak'), ('GF', 'Golf'), ('FB', 'Futbol'), ('BW', 'Bowling'), ('BL', 'Bilardo'), ('BB', 'Beyzbol'), ('BBO', 'Basketbol'), ('BM', 'Badminton'), ('AI', 'Aikido')], verbose_name='Branş'),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(max_length=100, default=datetime.datetime(2016, 7, 10, 18, 10, 38, 114091), verbose_name='Kayıt Tarihi'),
        ),
    ]
