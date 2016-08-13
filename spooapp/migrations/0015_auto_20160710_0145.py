# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0014_auto_20160710_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitap',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('baslik', models.CharField(max_length=100)),
                ('tarih', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Yazar',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(verbose_name='Kayıt Tarihi', default=datetime.datetime(2016, 7, 10, 1, 45, 36, 449878), max_length=100),
        ),
        migrations.AddField(
            model_name='kitap',
            name='yazar',
            field=models.ForeignKey(to='spooapp.Yazar'),
        ),
    ]
