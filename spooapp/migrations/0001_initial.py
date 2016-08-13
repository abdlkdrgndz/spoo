# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SporDallar',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('spor_dali_adi', models.CharField(max_length=255)),
                ('spor_dali_foto', models.ImageField(upload_to='static/images/branslar')),
            ],
            options={
                'verbose_name': 'Branş',
                'verbose_name_plural': 'Branşlar',
            },
        ),
        migrations.CreateModel(
            name='Tesisler',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('isletme_adi', models.CharField(verbose_name='İşletme Adı', max_length=200)),
                ('isletme_link', models.CharField(verbose_name='İşletme Link Yapısı', help_text='Otomatik olarak işletme adına göre düzenlenir eğer düzenlenmediyse örn: www.spoo.com/isletmeler/istanbul-hali-saha', max_length=255)),
                ('isletme_sahip', models.CharField(verbose_name='İşletme Sahibi Adı-Soyadı', max_length=255)),
                ('isletme_sahip_eposta', models.EmailField(verbose_name='İşletme E-Posta Adresi', max_length=255)),
                ('isletme_sahip_telefon', models.IntegerField(verbose_name='İşletme Telefonu')),
                ('isletme_foto', models.ImageField(verbose_name='İşletme Fotoğraf', default='default.jpg', upload_to='static/images/isletmeler/', help_text='Hizmet sağladığınız işletmenize ait fotoğraf yükleyin.')),
                ('isletme_adres', models.CharField(verbose_name='İşletme Adresi', default='Adres bilginizi girin', max_length=255)),
                ('isletme_brans', models.CharField(verbose_name='İşletme Branşı', choices=[('FT', 'Futbol'), ('VB', 'Voleybol'), ('BT', 'Basketbol'), ('GK', 'Go-Kart'), ('TN', 'Tenis')], max_length=255)),
                ('isletme_hizmet_zaman', models.DateTimeField(verbose_name='Seans Saatleri')),
                ('isletme_hizmet_bedeli', models.DecimalField(verbose_name='Rezervasyon Bedeli', default='10.5', decimal_places=1, max_digits=300, help_text='Bir organizasyonun tam bedelini girin.')),
                ('isletme_hizmet_kesinti_oran', models.IntegerField(verbose_name='Rezervasyon Kesinti Bedeli', default='3', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], help_text='Hizmet iptali durumunda yapılacak kesinti bedelini girin. ')),
                ('isletme_indirim_oran', models.IntegerField(verbose_name='Hizmet İndirim Oranı (%)', default='0', null=True, help_text='Rezervasyın hizmet bedelinden yapılacak indirim oranını girin.')),
                ('isletme_onay', models.CharField(verbose_name='Onay Durumu', default='3', choices=[('1', 'Onay'), ('2', 'Ret'), ('3', 'Beklemede')], max_length=5)),
                ('isletme_degerlendirme', models.IntegerField(verbose_name='İşletme Puanı', default='1')),
                ('isletme_kaydeden_kullanici', models.CharField(verbose_name='Kullanıcı Adı', blank=True, max_length=255)),
                ('isletme_kayit_tarih', models.CharField(verbose_name='Kayıt Tarihi', default=datetime.datetime(2016, 7, 7, 16, 59, 8, 608759), max_length=100)),
            ],
            options={
                'verbose_name': 'Isletme',
                'verbose_name_plural': 'Isletmeler',
            },
        ),
        migrations.CreateModel(
            name='Uniteler',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('unite_adi', models.CharField(help_text='İşletmede sağlan hizmetleri seçin.', blank=True, null=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Ünite',
                'verbose_name_plural': 'Üniteler',
            },
        ),
    ]
