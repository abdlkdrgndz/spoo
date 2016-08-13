# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from .models import Tesisler, BransUcretleri, RezervasyonTalepler
from django.http import HttpResponse

#Bu form ile branş ücreti eklerken yalnızca kendi işletmesini görüntülemesini sağlarız.
# Yönetim paneline giriş yapan kişiye göre işletme adları ve işletme adına göre branşlar gelecek.

class RezervasyonTalepFormu(forms.ModelForm):
    class Meta:
        model = RezervasyonTalepler
        fields = [f.name for f in RezervasyonTalepler._meta.fields]


