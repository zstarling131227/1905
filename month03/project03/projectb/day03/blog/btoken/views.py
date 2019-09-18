import hashlib
import json
import time

from user.models import UserProfile
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def tokens(request):
    '''
    创建token==登录
    :param request:
    :return:
    '''
    if not request.method == "POST":
        result = {'code': 101, 'error': 'Please use POST!'}
        return JsonResponse(result)

    # #http://127.0.0.1:8000/v1/tokens（返回的是json数据类型）
    # #http://127.0.0.1:5000/login（返回的是前段页面类型）
    json_str = request.body
    if not json_str:
        result = {'code': 102, 'error': 'Please give me data!'}
        return JsonResponse(result)

    json_obj = json.loads(json_str)
    username = json_obj.get('username')
    if not username:
        result = {'code': 103, 'error': 'Please give me username!'}
        return JsonResponse(result)

    password = json_obj.get('password')
    if not password:
        result = {'code': 104, 'error': 'Please give me password!'}
        return JsonResponse(result)

    user = UserProfile.objects.filter(username=username)
    if not user:
        result = {'code': 105, 'error': 'username or password is wrong!'}
        return JsonResponse(result)

    user = user[0]
    m = hashlib.md5()
    m.update(password.encode())
    if m.hexdigest() != user.password:
        result = {'code': 106, 'error': 'username or password is wrong!'}
        return JsonResponse(result)

    token = make_token(username)
    result = {'code': 200, 'username': username, 'data': {'token': token.decode()}}
    return JsonResponse(result)


def make_token(username, expire=3600 * 24):
    import jwt  # #(局部引用)
    key = '1234567'
    now = time.time()
    payload = {'username': username, 'exp': int(now + expire)}
    return jwt.encode(payload, key, algorithm='HS256')
