'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''

from django.db import models


class UserRequest(models.Model):
    student_id = models.IntegerField(db_column='Student_id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)
    major = models.CharField(db_column='Major', max_length=10, blank=True, null=True)
    e_mail = models.CharField(db_column='E_Mail', max_length=30, blank=True, null=True)
    phone = models.IntegerField(db_column='Phone', blank=True, null=True)
    github = models.CharField(db_column='Github', max_length=30, blank=True, null=True)
    introduction = models.CharField(db_column='Introduction', max_length=100, blank=True, null=True)
    sns_address = models.CharField(db_column='SNS_address', max_length=50, blank=True, null=True)
