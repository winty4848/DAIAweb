'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''
from django.db import models

class Question(models.Model): # 회원가입 신청목록 ,회원목록 텍스트
    question_text=models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class User(models.Model):
    student_id = models.IntegerField(db_column='Student_id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)
    major = models.CharField(db_column='Major', max_length=10, blank=True, null=True)
    class_field = models.CharField(db_column='Class', max_length=100 , blank=True, null=True)
    e_mail = models.CharField(db_column='E_Mail', max_length=30, blank=True, null=True)
    phone = models.IntegerField(db_column='Phone', blank=True, null=True)
    github = models.CharField(db_column='Github', max_length=30, blank=True, null=True)
    introduction = models.CharField(db_column='Introduction', max_length=100, blank=True, null=True)
    sns_address = models.CharField(db_column='SNS_address', max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='member', null=True, blank=True)

    def __str__(self):
        return self.name
