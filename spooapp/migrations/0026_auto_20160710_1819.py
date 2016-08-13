# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0025_auto_20160710_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bransucretleri',
            name='brans_adi',
            field=models.CharField(blank=True, verbose_name='Branş', null=True, choices=[('AT', 'Atıcılık'), ('HT', 'Hentbol'), ('BP', 'Buz Pateni'), ('VB', 'Voleybol'), ('TN', 'Tenis'), ('PB', 'Paintball'), ('MT', 'Masa Tenisi'), ('KA', 'Kayak'), ('GF', 'Golf'), ('FB', 'Futbol'), ('BW', 'Bowling'), ('BL', 'Bilardo'), ('BB', 'Beyzbol'), ('BBO', 'Basketbol'), ('BM', 'Badminton'), ('AI', 'Aikido')], max_length=255),
        ),
        migrations.AlterField(
            model_name='bransucretleri',
            name='brans_ucreti',
            field=models.DecimalField(default='10.5', verbose_name='Ücret', decimal_places=1, max_digits=300, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 10, 18, 19, 0, 363780), verbose_name='Kayıt Tarihi', max_length=100),
        ),
    ]
