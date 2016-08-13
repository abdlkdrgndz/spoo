# -*- coding: utf-8 -*-

import datetime
from django.core.serializers import json
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_http_methods
from django.views.generic import  CreateView
from .models import Tesisler, SporDallar, RezervasyonTalepler
from .forms import RezervasyonTalepFormu
from django.contrib.auth import authenticate, login



def Giris(request):
    return HttpResponse('Merhaba')

#Anasayfanın görüntülenmesi
def Index(request):
    branslar = SporDallar.objects.all().order_by('spor_dali_adi')
    return render_to_response('index.html', {'brans' : branslar}  , context_instance=RequestContext(request))


#Tesislerin görüntülenmesi, aranması ile çıkan sonuçları listeler.
def tesisler_listesi(request, gelen):
    if request.method == 'GET':
        #return HttpResponse(request.method)
        bul = Tesisler.objects.filter(bransucretleri__brans_adi__contains=gelen)
        if bul.count() > 0:
            return render_to_response('tesisler.html', {'arananlar' : bul},  context_instance=RequestContext(request))
        else:
            return render_to_response('tesisler.html', {'tesis_yok' : 'başarısız'}, context_instance=RequestContext(request))
    else:
        return render_to_response('tesisler.html', context_instance=RequestContext(request))


def Hareketler(request):
    return render_to_response('hareketler.html', context_instance=RequestContext(request))


@csrf_exempt
def rezervasyontalepkayit(request):
    if request.is_ajax():
        gelen = request.POST.get('st_id')
        if gelen is None:
            return HttpResponse(status=400)
        else:
            return JsonResponse({'sonuc': gelen })
    else:
        return JsonResponse({'sonuc': 'gönderilen bir değer yok' })







