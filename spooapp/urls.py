from django.conf.urls import include, url
from .views import Giris, Index, tesisler_listesi, Hareketler, rezervasyontalepkayit

urlpatterns = [
    url(r'^$', Index ),
    url(r'^tesisler/(?P<gelen>.+$)', tesisler_listesi, name='ts'),
    url(r'^hareketler/$', Hareketler ),
    url(r'^tesisler/rezervasyon_talep/$', rezervasyontalepkayit, name='rez_talep'),

]
