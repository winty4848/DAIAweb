'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''
from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^members/$', views.members, name='members'),
    url(r'^members/(?P<radix>\d+)/$', views.members_radix, name='members_radix'),

    url(r'^notice/$', views.notice, name='notice'),
    url(r'^notice/(?P<pk>\d+)/$', views.notice_detail, name='notice_detail'),
    url(r'^notice/new/$', views.notice_new, name='notice_new'),
    url(r'^notice/(?P<pk>\d+)/edit/$', views.notice_edit, name='notice_edit'),
    url(r'^notice/(?P<pk>\d+)/remove/$', views.notice_remove, name='notice_remove'),


    url(r'^project/$', views.project, name='project'),
    url(r'^project/(?P<pk>\d+)/$', views.project_detail, name='project_detail'),
    url(r'^project/new/$', views.project_new, name='project_new'),
    url(r'^project/(?P<pk>\d+)/edit/$', views.project_edit, name='project_edit'),
    url(r'^project/(?P<pk>\d+)/remove/$', views.project_remove, name='project_remove'),

    url(r'^seminar/$', views.seminar, name='seminar'),
    url(r'^seminar/(?P<pk>\d+)/$', views.seminar_detail, name='seminar_detail'),
    url(r'^seminar/new/$', views.seminar_new, name='seminar_new'),
    url(r'^seminar/(?P<pk>\d+)/edit/$', views.seminar_edit, name='seminar_edit'),
    url(r'^seminar/(?P<pk>\d+)/remove/$', views.seminar_remove, name='seminar_remove'),

    url(r'^recruit/$', views.recruit, name='recruit'),
    url(r'^about/$', views.about, name='about'),
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^album/$', views.album, name='album'),
    url(r'^album/(?P<pk>\d+)/$', views.album_detail, name='album_detail'),
    url(r'^album/new/$', views.album_new, name='album_new'),
    url(r'^album/(?P<pk>\d+)/edit/$', views.album_edit, name='album_edit'),
]
urlpatterns += static('media', document_root=settings.MEDIA_ROOT)