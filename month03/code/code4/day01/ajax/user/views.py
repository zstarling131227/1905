from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import User


def xhr(request):
    return render(request, 'xhr.html')


def get_xhr(request):
    return render(request, 'get-xhr.html')


def get_xhr_server(request):
    if request.GET.get('uname'):
        uname = request.GET['uname']
        return HttpResponse('WELCOME %s' % uname)
    return HttpResponse('This is ajax request!')


def register(request):
    return render(request, 'register.html')


def checkuname(request):
    uname = request.GET.get('uname')
    users = User.objects.filter(uname=uname).all()
    if users:
        return HttpResponse("用户名已存在")
    return HttpResponse('OK')


def make1_post(request):
    if request.method == 'GET':
        return render(request, 'make1_post.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        return HttpResponse("Your post is ok! %s %s" % (uname, pwd))


def make_post(request):
    if request.method == 'GET':
        return render(request, 'make_post.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        return HttpResponse("Your post is ok! %s %s" % (uname, pwd))
    # else:
        # raise
