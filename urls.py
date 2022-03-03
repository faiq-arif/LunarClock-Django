from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    url(r'^getPhase/$', views.getPhase, name='getPhase'),
    url(r'^getAlt/$', views.getAlt, name='getAlt'),
    url(r'^getAz/$', views.getAz, name='getAz'),
    url(r'^getImage/$', views.getImage, name='getImage'),
    url(r'^getElong/$', views.getElong, name='getElong'),
    url(r'^hDate/$', views.hDate, name='hDate'),
    url(r'^gDate/$', views.gDate, name='gDate'),
    url(r'^dayname/$', views.dayname, name='dayname'),
]
