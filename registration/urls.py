'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.loginin, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^info/$', views.info, name='info'),
    ]