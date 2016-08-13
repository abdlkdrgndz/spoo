# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0007_auto_20160707_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='RezervasyonTalepler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('r_kullanici_adi', models.CharField(verbose_name='Kullanıcı Adı', help_text='Rezervasyon talebinde bulunan kullanıcı adı', max_length=255)),
                ('r_isletme_kadi', models.CharField(verbose_name='İşletme Sahibi', max_length=255)),
                ('r_isletme_adi', models.CharField(verbose_name='Rezervasyon talebinde bulunulan işletme', max_length=255)),
                ('r_kullanici_telefon', models.IntegerField(verbose_name='Kullanıcı Telefonu')),
                ('r_tarihi', models.CharField(verbose_name='Rezervasyon Tarihi', help_text='Talep edilen rezervasyon tarihi', max_length=255)),
                ('r_onay_durumu', models.CharField(verbose_name='Rezervasyon Onayı', choices=[('O', 'Onay'), ('R', 'Ret')], help_text='Rezervasyon talebi onay/ret', max_length=255)),
                ('r_oneri', models.TextField(verbose_name='Öneri Notu', help_text='Kullanıcıya yeni bir rezervasyon tarihi önerebilir veya farklı öneri notları gönderebilirsiniz.')),
            ],
            options={
                'verbose_name': 'Rezervasyon Talebi',
                'verbose_name_plural': 'Rezervasyon Talepleri',
                'ordering': ['-r_tarihi'],
            },
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(verbose_name='Kayıt Tarihi', max_length=100, default=datetime.datetime(2016, 7, 8, 0, 7, 4, 557635)),
        ),
    ]
