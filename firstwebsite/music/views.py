# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader
def index(request):
    all_albums = Album.objects.all()
    print (all_albums)

    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums
    }
    #return HttpResponse("<h2>Details for Album id </h2>")
    #return HttpResponse(template.render(context,request))
    return HttpResponse(template.render(context, request))
    #html =''
    #for album in all_albums:
    #    url = '/music/' + str(album.id) + '/'
    #    html += '<a href="'+ url + '">'+ album.album_title+'</a><br>'
    #<li><a href="/music/1/"> text</a></li>

    return HttpResponse(html)
def detail(request, album_id):
    print str(album_id)
    return HttpResponse("<h2>" +str(album_id) + "</h2>")
# Create your views here.
