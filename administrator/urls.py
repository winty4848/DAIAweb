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

urlpatterns = [
    url(r'^administrator/$', views.administrator, name='administrator'),
    url(r'^administrator/(?P<userRequest_student_id>\d+)/okay/$', views.okay, name='okay'),
    url(r'^administrator/(?P<user_student_id>\d+)/detail/$',views.detail,name='detail'),
    url(r'^administrator/(?P<user_student_id>\d+)/modify/$',views.modify,name='modify'),
]