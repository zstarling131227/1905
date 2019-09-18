import json
import jwt
from django.shortcuts import render
from django.http import JsonResponse
import hashlib

# Create your views here.
def users(request):
    if request.method == 'GET':
        return JsonResponse({'code': 200})
    elif request.method == 'POST':
        # #报错，因为request.POST()只适用于表单数据的提交
        # #print(request.POST['username'])
        # #前段页面注册地址http://127.0.0.1:5000/register
        # #用如下方法打印，会打印出一个字节串
        print(request.body)
        dict=json.loads(request.body)
        jwt.encode()
        return JsonResponse({'code': 200, 'username': "xixi", 'data': {'token': 'abcdef'}})
    elif request.method == 'PUT':
        pass
    else:
        raise ValueError

    return JsonResponse({'code': 200})
