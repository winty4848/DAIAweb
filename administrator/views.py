'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''
from django.shortcuts import get_object_or_404,render
from .models import Question,User
from registration.models import UserRequest
from .forms import UserInfoForm
from django.shortcuts import redirect

def administrator(request):
    latest_question_list0 = Question.objects.all()[0]
    latest_question_list1 = Question.objects.all()[1]
    latest_UserRequest_list = UserRequest.objects.all()
    latest_User_list = User.objects.all()

    context = {
        'latest_question_list0': latest_question_list0,
        'latest_question_list1': latest_question_list1,
        'latest_UserRequest_list': latest_UserRequest_list,
        'latest_User_list': latest_User_list,
    }

    return render(request,'administrator/admin_main.html',context)

def okay(request, userRequest_student_id):
    if request.method == 'POST' and 'btn1' in request.POST:
        userRequest = UserRequest.objects.get(student_id=userRequest_student_id)
        user = User()
        user.name = userRequest.name
        user.e_mail = userRequest.e_mail
        user.github = userRequest.github
        user.major = userRequest.major
        user.sns_address = userRequest.sns_address
        user.student_id = userRequest.student_id
        user.phone = userRequest.phone
        user.introduction = userRequest.introduction
        # user.image = userRequest.image
        user.save()

        userRequest.delete()
        return redirect('administrator')

    elif request.method == 'POST' and 'btn2' in request.POST:
        deny = UserRequest.objects.get(student_id=userRequest_student_id)
        return redirect('administrator')


def detail(request,user_student_id):
    user = User.objects.get(student_id=user_student_id)
    form_class = UserInfoForm(initial=
                               {'student_id':user.student_id,
                                'name':user.name,
                                'e_mail':user.e_mail,
                                'github': user.github,
                                'sns_address': user.sns_address,
                                'phone': user.phone,
                                'major': user.major,
                                'class_field': user.class_field,
                                'introduction' : user.introduction,
                                'image': user.image
                                })
    context = {
        'user': user,
        'form': form_class,
    }

    return render(request,'administrator/detail.html',context)

def modify(request, user_student_id):
    member = User.objects.filter(student_id=user_student_id)
    if request.method == 'POST' and 'btn1' in request.POST:
        form = UserInfoForm(request.POST)
        form.save()
        return redirect('administrator')

    elif request.method == 'POST' and 'btn2' in request.POST:
        member = User.objects.get(student_id = user_student_id)
        return redirect('administrator')