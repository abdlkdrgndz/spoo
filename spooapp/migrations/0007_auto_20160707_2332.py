# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('spooapp', '0006_auto_20160707_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_hizmet_kesinti_oran',
            field=models.IntegerField(default='3', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Rezervasyon İptal Kesinti Bedeli', help_text='Hizmet iptali durumunda yapılacak kesinti bedelini girin. '),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='isletme_kayit_tarih',
            field=models.CharField(default=datetime.datetime(2016, 7, 7, 23, 32, 38, 913691), verbose_name='Kayıt Tarihi', max_length=100),
        ),
    ]
