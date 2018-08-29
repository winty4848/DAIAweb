'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''

from django import forms
from .models import UserRequest

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ['student_id', 'name', 'major', 'e_mail', 'password',
                  'phone', 'github', 'introduction', 'sns_address',
                  ]

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ['student_id', 'password']