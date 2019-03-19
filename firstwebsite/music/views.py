# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader

def index(request):
    return HttpResponse("<h2>Filler Text</h2>")

def detail(request, album_id):
    print str(album_id)
    return HttpResponse("<h2>" +str(album_id) + "</h2>")
# Create your views here.
