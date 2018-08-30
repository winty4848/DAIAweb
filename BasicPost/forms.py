'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''
from django import forms
from .models import Gallary, ProjectBoard, SeminarBoard, NoticeBoard

class GallaryForm(forms.ModelForm):
    class Meta:
        model = Gallary
        fields = ('title','content')

class ProjectBoardForm(forms.ModelForm):
    class Meta:
        model = ProjectBoard
        fields = ('title','content','project_member','process','image','file')

class SeminarBoardForm(forms.ModelForm):
    class Meta:
        model = SeminarBoard
        fields = ('title','content','image','file')

class NoticeBoardForm(forms.ModelForm):
    class Meta:
        model = NoticeBoard
        fields = ('title','content','image','file')