# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader

def index(request):
    return HttpResponse("<h2>Details for Album id </h2>")

def detail(request, album_id):
    print album_id
    return HttpResponse("<h2>Details for Album id " +str(album_id) + "</h2>")
# Create your views here.
