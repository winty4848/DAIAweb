'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import SignupForm, LoginForm
from .models import UserRequest
from administrator.models import User
from administrator.forms import UserInfoForm



def signup(request):
    # id, pwd, etc rule check

def loginin(request):
    # login id, pwd check

def logout(request):
    # del something
    return redirect('index')

def info(request):
    if request.method == "POST":
            return redirect('index')
    else:
        return render(request, 'registration/info.html') #, 'form': form})