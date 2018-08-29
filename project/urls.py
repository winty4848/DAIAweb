'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views


urlpatterns = [
    url(r'', include('BasicPost.urls')),
    url(r'', include('registration.urls')),
    url(r'', include('administrator.urls')),
]