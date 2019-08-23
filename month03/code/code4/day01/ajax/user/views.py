import json

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

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
    # return render(request, 'register.html')
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        if not uname:
            return HttpResponse("请输入用户名")
        pwd = request.POST.get('pwd')
        if not pwd:
            return HttpResponse("请输入密码")
        nickname = request.POST.get('nickname')
        if not nickname:
            return HttpResponse("请输入昵称")
        try:
            User.objects.create(uname=uname, pwd=pwd, nickname=nickname)
        except Exception as err:
            return HttpResponse('注册失败，请稍后重试！')
        return HttpResponse('注册成功！')


def checkuname(request):
    uname = request.GET.get('uname')
    users = User.objects.filter(uname=uname).all()
    if users:
        return HttpResponse("1")
    return HttpResponse('0')


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


def get_user(request):
    return render(request, 'get_user.html')


def get_user_server(request):
    users = User.objects.all()
    msg = ''
    for u in users:
        msg += '%s_%s_%s|' % (u.uname, u.pwd, u.nickname)
    msg = msg[:-1]
    return HttpResponse(msg)


def json_obj(request):
    return render(request, 'json_obj.html')


def json_dumps(request):
    dic = {
        'uname': 'lili',
        'uage': '30',
    }
    json_str = json.dumps(dic, sort_keys=True, separators=(',', ':'))
    # return HttpResponse(json_str)

    s = [
        {
            'uname': 'yaoyue',
            'uage': 23,
        },
        {
            'uname': 'xixi',
            'uage': 24,
        }
    ]
    json_str_arr = json.dumps(s)
    # return HttpResponse(json_str_arr, content_type='application/json')


    from django.core import serializers
    users=User.objects.all()
    json_str_all=serializers.serialize('json',users)
    return HttpResponse(json_str_all, content_type='application/json')


    # 用非serializers得到相同结果方法
    l=[]
    users=User.objects.all()
    for i in users:
        d={}
        d['username']=i.name
        l.append(d)
    all_json=json.dumps(l)
    return HttpResponse(all_json, content_type='application/json')

    # return JsonResponse({'UNMAE':'wulaio'})
    # return JsonResponse(s)#内部只能存字典，不能存字符串
    # return JsonResponse({'code':10010,'data':{}})