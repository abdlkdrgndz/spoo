# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0010_auto_20160708_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='BransUcretleri',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('brans_ucreti', models.DecimalField(default='10.5', verbose_name='Ücret', max_digits=300, decimal_places=1)),
                ('kullanici_adi', models.CharField(max_length=255, verbose_name='Kullanıcı Adı')),
                ('brans_adi', models.ForeignKey(verbose_name='Branş', to='spooapp.SporDallar')),
            ],
            options={
                'verbose_name': 'Branş Ücreti',
                'ordering': ['kullanici_adi'],
                'verbose_name_plural': 'Branş Ücretleri',
            },
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(max_length=100, default=datetime.datetime(2016, 7, 9, 11, 18, 9, 112613), verbose_name='Kayıt Tarihi'),
        ),
    ]
