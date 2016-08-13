# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from django.db.models import Q
from django.http import request
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User, auth

# Diğer Özellikler burada yer alır.

onay_durumu = (('1', 'Onay'), ('2', 'Ret'), ('3', 'Beklemede'))
simdiki_zaman =  datetime.now()

#İşletmelerin sağlamış olduğu hizmetlere dair bilgilerin girildiği alandır.
class Uniteler(models.Model):
    unite_adi                   = models.CharField(max_length=255, null=True, blank=True, help_text='İşletmede sağlan hizmetleri seçin.')

    def __str__(self):
        return self.unite_adi

    class Meta:
        verbose_name            = 'Ünite'
        verbose_name_plural     = 'Üniteler'

# Tüm aktivite ve spor dalları ile ilgili bilgilerin girildiği alandır.
class SporDallar(models.Model):
    spor_dali_adi               = models.CharField(max_length=255)
    spor_dali_foto              = models.ImageField(upload_to='static/images/branslar')

    def __str__(self):
        return self.spor_dali_adi

    class Meta:
        verbose_name            = 'Branş'
        verbose_name_plural     = 'Branşlar'


class Tesisler(models.Model):
    isletme_adi                 = models.CharField(max_length=200, verbose_name='İşletme Adı')
    isletme_link                = models.CharField(max_length=255, verbose_name='İşletme Link Yapısı', help_text='Otomatik olarak işletme adına göre düzenlenir eğer düzenlenmediyse örn: www.spoo.com/isletmeler/istanbul-hali-saha')
    isletme_sahip               = models.CharField(max_length=255, verbose_name='İşletme Sahibi Adı-Soyadı')
    isletme_sahip_eposta        = models.EmailField(max_length=255, verbose_name='İşletme E-Posta Adresi')
    isletme_sahip_telefon       = models.IntegerField(verbose_name='İşletme Telefonu')
    isletme_foto                = models.ImageField(upload_to='static/images/isletmeler/', verbose_name='İşletme Fotoğraf', help_text='Hizmet sağladığınız işletmenize ait fotoğraf yükleyin.', null=False, default='default.jpg')
    isletme_adres               = models.CharField(max_length=255, verbose_name='İşletme Adresi', default='Adres bilginizi girin')
    isletme_hizmetleri          = models.ManyToManyField(Uniteler)
    #isletme_hizmet_zaman        = models.DateTimeField(verbose_name='Seans Başlangıcı', help_text='Rezervasyon saatlerinin başlangıç ve bitiş saatlerini belirleyin.')
    #isletme_hizmet_bitis        = models.DateTimeField(verbose_name='Seans Bitişi', null=True)
    isletme_onay                = models.CharField(max_length=5, choices=onay_durumu, verbose_name='Onay Durumu', default='3')
    isletme_degerlendirme       = models.IntegerField(verbose_name='İşletme Puanı', default='1')
    isletme_kaydeden_kullanici  = models.CharField(max_length=255, blank=True, verbose_name='Kullanıcı Adı')
    isletme_kayit_tarih         = models.CharField(max_length=100, default=simdiki_zaman, verbose_name='Kayıt Tarihi')


    def __str__(self):
        return self.isletme_adi


    class Meta:
        verbose_name            = 'Isletme'
        verbose_name_plural     = 'Isletmeler'

#Kullanıcılardan gelen rezervasyon taleplerinin yönetildiği alandır.
class RezervasyonTalepler(models.Model):
    r_kullanici_adi             = models.CharField(max_length=255, verbose_name='Kullanıcı Adı', help_text='Rezervasyon talebinde bulunan kullanıcı adı')
    r_isletme_kadi              = models.CharField(max_length=255, verbose_name='İşletme Sahibi')
    r_isletme_adi               = models.CharField(max_length=255, verbose_name='Rezervasyon Talebinde Bulunulan İşletme')
    r_isletme_brans             = models.CharField(max_length=255, verbose_name='Branş', null=True)
    r_kullanici_telefon         = models.IntegerField(verbose_name='Kullanıcı Telefonu')
    r_tarihi                    = models.CharField(max_length=255, verbose_name='Rezervasyon Tarihi', help_text='Talep edilen rezervasyon tarihi')
    r_onay_durumu               = models.CharField(max_length=255, verbose_name='Rezervasyon Onayı', choices=(('O', 'Onay'), ('R', 'Ret'), ('B', 'Beklemede')), help_text='Rezervasyon talebi onay/ret')
    r_oneri                     = models.TextField(verbose_name='Öneri Notu', help_text='Kullanıcıya yeni bir rezervasyon tarihi önerebilir veya farklı öneri notları gönderebilirsiniz.')

    def __str__(self):
        return self.r_kullanici_adi

    class Meta:
        ordering                = ['-r_tarihi']
        verbose_name            = 'Rezervasyon Talebi'
        verbose_name_plural     = 'Rezervasyon Talepleri'

branslar = (
    ('Atıcılık', 'Atıcılık'),
    ('Hentbol', 'Hentbol'),
    ('Buz Pateni', 'Buz Pateni'),
    ('Voleybol', 'Voleybol'),
    ('Tenis', 'Tenis'),
    ('Paintball', 'Paintball'),
    ('Masa Tenisi', 'Masa Tenisi'),
    ('Kayak', 'Kayak'),
    ('Golf', 'Golf'),
    ('Futbol', 'Futbol'),
    ('Bowling', 'Bowling'),
    ('Bilardo', 'Bilardo'),
    ('Beyzbol', 'Beyzbol'),
    ('Basketbol', 'Basketbol'),
    ('Badminton', 'Badminton'),
    ('Aikido', 'Aikido')
)
#İşletmelerin vermiş olduğu branşların fiyatlandırma bilgileri eklenir/düzenlenir.
class BransUcretleri(models.Model): #1
    isletme_adi                 = models.ForeignKey(Tesisler, verbose_name='İşletme Adı')
    brans_adi                   = models.CharField(max_length=255, choices=branslar,  verbose_name='Branş', null=True, blank=True)
    brans_ucreti                = models.DecimalField(verbose_name='Ücret', max_digits=300, decimal_places=1, default='10.5', null=True, blank=True)


    def __str__(self):
        return self.brans_adi

    class Meta:
        verbose_name            = 'Branş Ücreti'
        verbose_name_plural     = 'Branş Ücretleri'











