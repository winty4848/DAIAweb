'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''
from django.utils import timezone
from BasicPost.models import Gallary,Images, ProjectBoard, SeminarBoard, NoticeBoard
from administrator.models import User
from django.shortcuts import render, get_object_or_404
from .forms import GallaryForm, ProjectBoardForm,SeminarBoardForm, NoticeBoardForm
from django.shortcuts import redirect
## 페이지네이션 구현
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
## 이미지 여러개 위한것
from django.forms import modelformset_factory

'''
del_file, del_image
When someone edits post, delete old file/image 
'''
def del_file(old_file, new_file):
    if old_file != new_file:
        old_file.delete()
    return new_file

def del_image(old_image, new_image):
    if old_image.name != new_image.name:
        old_image.delete()
    return new_image


# Create your views here.
def index(request):
    '''
    In main page, this view calls recent 4 posts.
    '''
    notices = NoticeBoard.objects.all().order_by('-origin_date')
    projects = ProjectBoard.objects.all().order_by('-origin_date')
    seminars = SeminarBoard.objects.all().order_by('-origin_date')
    return render(request, 'blog/index.html', {'notices': notices, 'projects': projects, 'seminars':seminars})

def album(request):
    gallaries = Gallary.objects.all().order_by('-origin_date')
    paginator = Paginator(gallaries, 6)
    page = request.GET.get('page')

    try:
        gallaries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        gallaries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        gallaries = paginator.page(paginator.num_pages)

    max_index = len(paginator.page_range)
    return render(request, 'blog/album.html', {
        'gallaries': gallaries,
        'max_index' : max_index,
    })

def album_new(request):
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=5, max_num=5)
    if request.method == "GET":
        form = GallaryForm()
        formset = ImageFormset(queryset=Images.objects.none())
    elif request.method == "POST":
        form = GallaryForm(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            gallary = form.save(commit=False)
            gallary.origin_date = timezone.now()
            gallary.final_date=timezone.now()
            gallary.save()

            for f in formset:
                try:
                    photo=Images(post=gallary, image=f.cleaned_data['image'])
                    photo.save()

                except Exception as e:
                    break
            return redirect('album')
    return render(request, 'blog/album_edit.html',
                  {'form': form, 'formset': formset})


def album_detail(request, pk):
    gallary = get_object_or_404(Gallary, pk=pk)
    return render(request, 'blog/album_detail.html', {'gallary': gallary})



def album_edit(request, pk):
    gallary = get_object_or_404(Gallary, pk=pk)
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=5, max_num=5)
    if request.method == "POST":
        form = GallaryForm(request.POST or None, instance=gallary)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            gallary = form.save(commit=False)
            gallary.final_date = timezone.now()
            gallary.save()
            # image check - 프롬프트 창 확인
            print(formset.cleaned_data)
            data=Images.objects.filter(post=gallary)
            for index, f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        photo = Images(post=gallary, image=f.cleaned_data['image'])
                        photo.save()
                    elif f.cleaned_data['image'] is False:
                        photo = Images.objects.get(id=request.POST.get('form-' + str(index) + '-id'))
                        photo.delete()
                    else:
                        photo = Images(post=gallary, image=f.cleaned_data['image'])
                        d=Images.objects.get(id=data[index].id)
                        d.image=photo.image
                        d.save()
            return redirect(album)
    else:
        form = GallaryForm(instance=gallary)
        formset = ImageFormset(queryset=Images.objects.filter(post=gallary))
    return render(request, 'blog/album_edit.html', {'gallary': gallary, 'form': form, 'formset': formset})

def album_remove(request, pk):
    post = get_object_or_404(Gallary, pk=pk)
    post.delete()
    return redirect('album')


def members(request):
    members = User.objects.order_by('class_field')

    return render(request, 'blog/members.html', {'members': members})

def members_radix(request, radix):
    str_radix=", "+str(radix)+"기"
    members_radix = User.objects.filter(class_field__contains=str_radix)
    print(members_radix[0].class_field)

    return render(request, 'blog/members_radix.html', {'members_radix': members_radix, 'radix': members_radix[0].class_field})

def notice(request):
    posts = NoticeBoard.objects.all().order_by('-origin_date')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    max_index = len(paginator.page_range)
    return render(request, 'blog/notice.html', {
        'posts': posts,
        'max_index': max_index,
    })



def notice_new(request):
    if request.method == "GET":
        form = NoticeBoardForm()
    elif request.method == "POST":
        form = NoticeBoardForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.origin_date = timezone.now()
            post.final_date = timezone.now()
            post.save()
            return redirect(notice)
    ctx = {
        'form': form,
    }

    return render(request, 'blog/notice_edit.html', ctx)

def notice_edit(request, pk):
    post = get_object_or_404(NoticeBoard, pk=pk)
    old_image = post.image
    old_file=post.file
    if request.method == "POST":
        form = NoticeBoardForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.final_date = timezone.now()
            new_image=post.image
            new_file=post.file
            post.image=del_image(old_image, new_image)
            post.file=del_file(old_file, new_file)
            post.save()
            return redirect('notice_detail', pk=post.pk)
    else:
        form = NoticeBoardForm(instance=post)
    return render(request, 'blog/notice_edit.html', {'post': post,'form': form})

def notice_detail(request, pk):
    post = get_object_or_404(NoticeBoard, pk=pk)
    return render(request, 'blog/notice_detail.html', {'post': post})

def seminar(request):
    posts = SeminarBoard.objects.all().order_by('-origin_date')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    max_index = len(paginator.page_range)
    return render(request, 'blog/seminar.html', {
        'posts': posts,
        'max_index': max_index,
    })



def seminar_new(request):
    if request.method == "GET":
        form = SeminarBoardForm()
    elif request.method == "POST":
        form = SeminarBoardForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.origin_date = timezone.now()
            post.final_date = timezone.now()
            post.save()
            return redirect(seminar)
    ctx = {
        'form': form,
    }

    return render(request, 'blog/seminar_edit.html', ctx)


def seminar_detail(request, pk):
    post = get_object_or_404(SeminarBoard, pk=pk)
    return render(request, 'blog/seminar_detail.html', {'post': post})



def seminar_edit(request, pk):
    post = get_object_or_404(SeminarBoard, pk=pk)
    old_image = post.image
    old_file = post.file

    if request.method == "POST":
        form = SeminarBoardForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.final_date = timezone.now()
            new_image=post.image
            new_file=post.file
            post.image=del_image(old_image, new_image)
            post.file=del_file(old_file, new_file)
            post.save()
            return redirect('seminar_detail', pk=post.pk)
    else:
        form = SeminarBoardForm(instance=post)
    return render(request, 'blog/seminar_edit.html', {'post': post,'form': form})


def project(request):
    posts = ProjectBoard.objects.all().order_by('-origin_date')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    max_index = len(paginator.page_range)
    return render(request, 'blog/project.html', {
        'posts': posts,
        'max_index': max_index,
    })



def project_new(request):
    if request.method == "GET":
        form = ProjectBoardForm()
    elif request.method == "POST":
        form = ProjectBoardForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.origin_date = timezone.now()
            post.final_date = timezone.now()
            post.save()
            return redirect(project)
    ctx = {
        'form': form,
    }

    return render(request, 'blog/project_edit.html', ctx)


def project_detail(request, pk):
    post = get_object_or_404(ProjectBoard, pk=pk)
    return render(request, 'blog/project_detail.html', {'post': post})



def project_edit(request, pk):
    post = get_object_or_404(ProjectBoard, pk=pk)
    old_image = post.image
    old_file = post.file
    if request.method == "POST":
        form = ProjectBoardForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.final_date = timezone.now()
            new_image=post.image
            new_file=post.file
            post.image=del_image(old_image, new_image)
            post.file=del_file(old_file, new_file)
            post.save()
            return redirect('project_detail', pk=post.pk)
    else:
        form = ProjectBoardForm(instance=post)
    return render(request, 'blog/project_edit.html', {'post': post,'form': form})


def recruit(request):
    return render(request, 'blog/recruit.html')


def about(request):
    return render(request, 'blog/about.html')


def rules(request):
    return render(request, 'blog/rules.html')


