import hashlib
import json
import time

from django.http import JsonResponse
from django.shortcuts import render
from btoken.views import make_token
from .models import *
from tools.login_check import login_check


# Create your views here.
# （就是不带参数的）# #访问的是http://127.0.0.1:8000/v1/users
def users1(request):
    pass


# （带参数的函数使用）# #访问的是http://127.0.0.1:8000/v1/users/<username>
def users_detail(request, username):
    pass


# 为了不影响根目录的使用（也就是不带参数的），需要添加一个参数并给定默认值（关键字传参）。
@login_check('PUT')
def users(request, username=None):
    if request.method == 'GET':
        # 获取用户数据(测试：带参数和不带参数)
        # if username:  # #访问的是http://127.0.0.1:8000/v1/users/<username>
        #     return JsonResponse({'code': 200, 'error': 'Welcome Get %s!' % username})
        # else:  # #访问的是http://127.0.0.1:8000/v1/users
        #     return JsonResponse({'code': 200, 'error': 'Welcome Get!'})

        # 获取用户数据(正式代码：获取响应格式)
        if username:
            try:
                user = UserProfile.objects.get(username=username)
            except Exception as e:
                user = None
            if not user:
                result = {'code': 208, 'error': 'The username is not exist!'}
                return JsonResponse(result)
            # #判断是否带有查询字符串
            # http://127.0.0.1:5000/xixi/info
            if request.GET.keys():  # #查询指定参数http://127.0.0.1:8000/v1/users/xixi?nickname=1&info=1
                data = {}
                for k in request.GET.keys():
                    if hasattr(user, k):  # # 判断数据表中是否有该字段名。在shell交互模式中先导入from user.models import UserProfile
                        v = getattr(user, k)  # # 获取数据表中该字段名的对应值
                        if k == 'avatar':
                            data[k] = str(k)
                        else:
                            data[k] = v

                result = {'code': 200,
                          'username': username,
                          'data': data
                          }
                return JsonResponse(result)
            else:  # #查询全量参数 http://127.0.0.1:8000/v1/users/xixi
                # #图片返回的是图片路径
                result = {'code': 200,
                          'username': username,
                          'data': {
                              'nickname': user.nickname,
                              'sign': user.sign,
                              'avatar': str(user.avatar),
                              'info': user.info}
                          }
                return JsonResponse(result)
        else:
            return JsonResponse({'code': 200, 'error': 'Welcome Get!'})

    # #http://127.0.0.1:5000/xixi/info
    elif request.method == 'POST':
        # 此功能模块异常码  201 开始
        # request.POST  只能拿表单post提交的数据
        # 创建用户
        # 前端注册页面地址  http://127.0.0.1:5000/register
        # print(request.body)
        # dict = json.loads(request.body)
        # import jwt
        # jwt.encode()

        json_str = request.body
        print(json_str)
        # 输出结果为：b'{"username":"yaoyue","email":"123@tedu.cn","password_1":"123","password_2":"123"}'
        if not json_str:
            result = {'code': 201, 'error': 'Please give me data!'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)
        username = json_obj.get('username')
        if not username:
            result = {'code': 202, 'error': 'Please give me username!'}
            return JsonResponse(result)

        email = json_obj.get('email')
        if not email:
            result = {'code': 203, 'error': 'Please give me email!'}
            return JsonResponse(result)

        password_1 = json_obj.get('password_1')
        password_2 = json_obj.get('password_2')
        if not password_1 or not password_2:
            result = {'code': 204, 'error': 'Please give me password!'}
            return JsonResponse(result)
        if password_1 != password_2:
            result = {'code': 205, 'error': 'The password is not same !'}
            return JsonResponse(result)

        # 用get时必须用try一下
        # old_user=UserProfile.objects.get()
        # 查询用户名是否已存在
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 206, 'error': 'The username is already existed!'}
            return JsonResponse(result)

        m = hashlib.md5()
        m.update(password_1.encode())
        sign = info = ''
        try:
            UserProfile.objects.create(username=username, nickname=username, password=m.hexdigest(), sign=sign,
                                       info=info, email=email)
        except Exception as e:
            result = {'code': 207, 'error': 'Server is busy!'}
            return JsonResponse(result)

        # 此时一定注册成功
        token = make_token(username)
        # token_de=token.decode()
        # print(token_de)
        result = {'code': 200, 'username': username, 'data': {'token': token.decode()}}
        return JsonResponse(result)

    # #http://127.0.0.1:5000/xixi/change_info
    elif request.method == 'PUT':
        # 更新数据
        request.META.get('HTTP_AUTHORIZATION')
        user = request.user
        print('-----------')
        print(user)
        print('-----------')
        json_str = request.body
        if not json_str:
            result = {'code': 209, 'error': 'Please give me data!'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)
        if 'sign' not in json_obj:
            result = {'code': 210, 'error': 'Please give me sign!'}
            return JsonResponse(result)
        if 'info' not in json_obj:
            result = {'code': 211, 'error': 'Please give me info!'}
            return JsonResponse(result)

        sign = json_obj.get('sign')
        info = json_obj.get('info')
        request.user.sign = sign
        request.user.info = info
        request.user.save()
        result = {'code': 200, 'username': request.user.username}
        return JsonResponse(result)

    else:
        raise ValueError
