# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0024_auto_20160710_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bransucretleri',
            name='brans_adi',
            field=models.CharField(verbose_name='Branş', null=True, max_length=255, choices=[('AT', 'Atıcılık'), ('HT', 'Hentbol'), ('BP', 'Buz Pateni'), ('VB', 'Voleybol'), ('TN', 'Tenis'), ('PB', 'Paintball'), ('MT', 'Masa Tenisi'), ('KA', 'Kayak'), ('GF', 'Golf'), ('FB', 'Futbol'), ('BW', 'Bowling'), ('BL', 'Bilardo'), ('BB', 'Beyzbol'), ('BBO', 'Basketbol'), ('BM', 'Badminton'), ('AI', 'Aikido')]),
        ),
        migrations.AlterField(
            model_name='bransucretleri',
            name='brans_ucreti',
            field=models.DecimalField(verbose_name='Ücret', null=True, max_digits=300, decimal_places=1, default='10.5'),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(verbose_name='Kayıt Tarihi', default=datetime.datetime(2016, 7, 10, 18, 11, 48, 890158), max_length=100),
        ),
    ]
