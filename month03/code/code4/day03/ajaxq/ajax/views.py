import json

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def load_test(request):
    return render(request, 'load_test.html')


def load_test_server(request):
    return render(request, 'load_test_server.html')


def jquery_get(request):
    return render(request, 'jquery_get.html')


def jquery_get_server(request):
    # 对应jquery_get.html中的无参script
    # d = {'uname': 'xixi', 'age': '34'}
    # # return HttpResponse(json.dumps(d))
    # # 指定httpresponse响应头
    # return HttpResponse(json.dumps(d), content_type='application/json')

    # 对应jquery_get.html中的有参script
    # 获取get请求参数
    uname = request.GET.get('uname', 'null')
    age = request.GET.get('age', 'null')
    d = {'uname': uname, 'age': age}
    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_post(request):
    return render(request, 'jquery_post.html')


def jquery_post_server(request):
    if int(request.POST.get('age', 0)) > 100:
        d = {'msg': 'your age is too old!!', 'code': 1201}
        return HttpResponse(json.dumps(d), content_type='application/json')
    d = {'msg': 'post is ok', 'code': 1200}
    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_ajax(request):
    return render(request, 'jquery_ajax.html')


def jquery_ajax_server(request):
    import time
    time.sleep(3)
    # raise
    d = {'name': 'xixi', 'age': '34'}
    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_ajax_user(request):
    return render(request, 'jquery_ajax_user.html')


def jquery_ajax_user_server(request):
    d = [{'name': '嘻嘻', 'age': '34'}, {'name': '钥玥', 'age': '24'}]
    return HttpResponse(json.dumps(d), content_type='application/json')


def cross(request):
    return render(request, 'cross.html')


def cross_server(request):
    func = request.GET.get('callback')
    return HttpResponse(func + "('welcome!')")


def cross_server_json(request):
    func = request.GET.get('callback')
    d = {'name': 'xixi', 'age': '34'}
    return HttpResponse(func + "(" + json.dumps(d) + ")")
