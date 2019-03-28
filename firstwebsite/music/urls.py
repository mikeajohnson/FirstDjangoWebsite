from django.conf.urls import url
from music import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    #/music/(album id)/
    url(r'^(?P<album_id>[0-9]+)/$',views.detail),

]
