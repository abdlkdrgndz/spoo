# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0027_auto_20160710_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bransucretleri',
            options={'verbose_name': 'Branş Ücreti', 'verbose_name_plural': 'Branş Ücretleri'},
        ),
        migrations.AlterField(
            model_name='bransucretleri',
            name='brans_adi',
            field=models.CharField(verbose_name='Branş', blank=True, max_length=255, null=True, choices=[('Atıcılık', 'Atıcılık'), ('Hentbol', 'Hentbol'), ('Buz Pateni', 'Buz Pateni'), ('Voleybol', 'Voleybol'), ('Tenis', 'Tenis'), ('Paintball', 'Paintball'), ('Masa Tenisi', 'Masa Tenisi'), ('Kayak', 'Kayak'), ('Golf', 'Golf'), ('Futbol', 'Futbol'), ('Bowling', 'Bowling'), ('Bilardo', 'Bilardo'), ('Beyzbol', 'Beyzbol'), ('Basketbol', 'Basketbol'), ('Badminton', 'Badminton'), ('Aikido', 'Aikido')]),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(max_length=100, default=datetime.datetime(2016, 7, 10, 22, 9, 4, 875425), verbose_name='Kayıt Tarihi'),
        ),
    ]
