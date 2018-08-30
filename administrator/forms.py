'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''
from django import forms
from .models import User

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields= 'student_id', 'name', 'major', 'class_field', 'e_mail', 'phone', 'github', 'introduction','image'
