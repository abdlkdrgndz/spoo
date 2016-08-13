# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0021_auto_20160710_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bransucretleri',
            options={'verbose_name_plural': 'Branş Ücretleri', 'ordering': ['brans_adi'], 'verbose_name': 'Branş Ücreti'},
        ),
        migrations.RemoveField(
            model_name='bransucretleri',
            name='kullanici_adi',
        ),
        migrations.AlterField(
            model_name='bransucretleri',
            name='brans_adi',
            field=models.CharField(max_length=255, verbose_name='Branş'),
        ),
        migrations.AlterField(
            model_name='bransucretleri',
            name='isletme_adi',
            field=models.ForeignKey(verbose_name='İşletme Adı', to='spooapp.Tesisler'),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(max_length=100, default=datetime.datetime(2016, 7, 10, 17, 42, 14, 710545), verbose_name='Kayıt Tarihi'),
        ),
    ]
