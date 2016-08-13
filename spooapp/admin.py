# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import Tesisler, SporDallar, Uniteler, RezervasyonTalepler, BransUcretleri



class BransInline(admin.StackedInline):
    model = BransUcretleri
    ordering = ['brans_adi']
    extra = 0

### Bu alanda işletmelerin eklenmesi, bilgilerinin güncellenmesi gibi yönetim işlemleri yapılır. ###

class IsletmeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tesisler._meta.fields]
    #fields = (('isletme_adi', 'isletme_link', 'isletme_sahip',  'isletme_sahip_eposta'),
              #('isletme_sahip_telefon', 'isletme_foto', 'isletme_adres'),  ('isletme_hizmetleri', 'isletme_brans'), ( 'isletme_hizmet_bedeli', 'isletme_hizmet_kesinti_oran', 'isletme_indirim_oran'),
              #('isletme_onay', 'isletme_degerlendirme', 'isletme_kaydeden_kullanici' , 'isletme_kayit_tarih'))
    list_per_page = 25
    filter_horizontal = ('isletme_hizmetleri', )
    inlines = [BransInline]

    # Tüm normal kullanıcılar Değerlendirme ve Onay Kısmına müdahale edemezler.
    def has_add_permission(self, request):
        if not request.user.is_superuser:
            IsletmeAdmin.readonly_fields = ['isletme_onay', 'isletme_degerlendirme', 'isletme_kaydeden_kullanici' , 'isletme_kayit_tarih']
            IsletmeAdmin.prepopulated_fields = {'isletme_link': ('isletme_adi',)}
            return True
        else:
            #super yetkili işletmenin bilgilerine müdahale edemez.
            IsletmeAdmin.readonly_fields=['isletme_sahip', 'isletme_adi', 'isletme_link', 'isletme_foto', 'isletme_sahip_eposta', 'isletme_sahip_telefon',
                                          'isletme_adres',  'isletme_hizmetleri',
                                           'isletme_kaydeden_kullanici', 'isletme_kayit_tarih' ]
            IsletmeAdmin.prepopulated_fields = {}
           #return True   işletme ekleme yetkisi super kullanıcıya verilemez.


    #İşletme kaydı yapılırken hangi kullanıcı tarafından kaydedildiğini tutalım.
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if getattr(obj, 'author', None) is None:
                obj.isletme_kaydeden_kullanici  = obj.isletme_kaydeden_kullanici
                obj.save()
        else:
            if getattr(obj, 'author', None) is None:
                obj.isletme_kaydeden_kullanici  = request.user.username
                obj.save()

    #super kullanıcı değilse sadece kendi kaydettiği işletmeleri gösterelim.
    def get_queryset(self, request):
        if not request.user.is_superuser:
            isletmeler = Tesisler.objects.filter(isletme_kaydeden_kullanici=request.user).order_by('isletme_kaydeden_kullanici')
            return isletmeler
        else:
            isletmeler = Tesisler.objects.all()
            return isletmeler


## SPOR DALLARI - BRANŞLAR

class SporDallarAdmin(admin.ModelAdmin):
    list_display = ['spor_dali_adi' ,'spor_dali_foto']

    # Normal kullanıcılar Spor Dallarının bulunduğu tabloyu göremezler.
    def has_module_permission(self, request):
        if not request.user.is_superuser:
            return False
        else:
            return True


class RezervasyonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in RezervasyonTalepler._meta.fields]
    #fields = [f.name for f in RezervasyonTalepler._meta.fields]
    filter       = ['r_onay_durumu']
    search_fields = ['r_kullanici_adi', 'r_tarihi']

    #super kullanıcı herhangi bir ekleme/silme yapamaz.
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return False

    # Normal kullanıcılar yalnızca kendi rezervasyon taleplerini görebilirler.
    def get_queryset(self, request):
        if not request.user.is_superuser:
            talepler = RezervasyonTalepler.objects.filter(r_isletme_kadi=request.user).order_by('r_tarihi')
            RezervasyonAdmin.readonly_fields = ['r_tarihi', 'r_kullanici_adi', 'r_isletme_kadi', 'r_isletme_adi', 'r_kullanici_telefon']
            return talepler
        else:
            talepler = RezervasyonTalepler.objects.all()
            RezervasyonAdmin.readonly_fields = [f.name for f in RezervasyonTalepler._meta.fields]
            return talepler



admin.site.register(Tesisler, IsletmeAdmin)
admin.site.register(SporDallar, SporDallarAdmin)
admin.site.register(Uniteler)
admin.site.register(RezervasyonTalepler,RezervasyonAdmin)

