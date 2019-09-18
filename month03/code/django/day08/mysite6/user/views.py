from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
# file: user/views.py
from . import models  # 导入模型模块

from django.contrib.auth.models import User

'''
def reg_view(request):
    dic = request.COOKIES
    print("COOIES=", str(dic))
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        # 验证数据的合法性
        if len(username) < 6:
            username_error = '用户名太短！'
            return render(request, 'user/register.html',
                          locals())
        # 验证密码１不能为空
        if len(password1) == 0:
            password_error = "密码不能为空"
            return render(request, 'user/register.html',
                          locals())
        # 验证两次密码必须一致
        if password1 != password2:
            password2_error = '两次密码不一致!'
            return render(request, 'user/register.html',
                          locals())
        # 检查数据库是否已有username这条记录，如果没有则完成注册
        try:
            auser = models.User.objects.get(
                username=username)
            username_error = "用户名已经存在!"
            return render(request, 'user/register.html',
                          locals())
        except:
            auser = models.User.objects.create(
                username = username,
                password = password1
            )
            html = """注册成功！<a href='/user/login'>
                    进入登陆</a>"""
            resp =  HttpResponse(html)
            # 添加cookies
            resp.set_cookie("username", username)
            return resp
'''

##修改版本
def reg_view(request):
   dic = request.COOKIES
   print("COOIES=", str(dic))
   if request.method == 'GET':
       return render(request, 'user/register.html')
   elif request.method == 'POST':
       username = request.POST.get('username', '')
       password1 = request.POST.get('password', '')
       password2 = request.POST.get('password2', '')
       # 验证数据的合法性
       if len(username) < 6:
           username_error = '用户名太短！'
           return render(request, 'user/register.html',
                         locals())
       # 验证密码１不能为空
       if len(password1) == 0:
           password_error = "密码不能为空"
           return render(request, 'user/register.html',
                         locals())
       # 验证两次密码必须一致
       if password1 != password2:
           password2_error = '两次密码不一致!'
           return render(request, 'user/register.html',
                         locals())
       # 检查数据库是否已有username这条记录，如果没有则完成注册
       try:
           auser = models.User.objects.get(
               username=username)
           username_error = "用户名已经存在!"
           return render(request, 'user/register.html',
                         locals())
       except:
           auser = User.objects.create_superuser(
               username = username,
               password = password1,
               email=''
           )
           html = """注册成功！<a href='/user/login'>
                   进入登陆</a>"""
           resp =  HttpResponse(html)
           # 添加cookies
           resp.set_cookie("username", username)
           return resp


def login_view(request):
   if request.method == 'GET':
       username = request.COOKIES.get('username', '')
       return render(request, 'user/login.html', locals())
   elif request.method == 'POST':
       username = request.POST.get('username', '')
       password1 = request.POST.get('password', '')
       if username == '':
           username_error = '用户名不能为空'
           return render(request, 'user/login.html',
                         locals())
       # 处理登陆的逻辑
       try: #（补充）
           auser = User.objects.get(
               username=username
           )
           # auser.check_password(password1)
           # 记录一个登陆状态
           request.session['user'] = {
               'username': username,
               'id': auser.id  # 记录当前用户的id
           }
           resp = HttpResponseRedirect('/')
           if 'remember' in request.POST:  # 选中状态
               resp.set_cookie('username', username)
           return resp
           # return HttpResponse("登陆成功")
       except:
           password_error = "用户名或密码不正确"
           return render(request, 'user/login.html',
                         locals())

def logout_view(request):
   '退出登陆'
   if 'user' in request.session:
       del request.session['user']  # 清除登陆记录
   return HttpResponseRedirect('/')  # 返回主页


   #　设置session的值
   # request.session['abc'] = 123
   # 获取：
   # val = request.session.get('abc', 'xxx')
   # print("val=", val)

   # return HttpResponse("添加成功")

from . import forms

def reg2_view(request):
   if request.method == 'GET':
       myform1 = forms.MyRegFrom()
       return render(request,
                     'user/reg2.html',
                     locals())
   elif request.method == 'POST':
       myform = forms.MyRegFrom(request.POST)
       if myform.is_valid():
           dic = myform.cleaned_data
           username = dic['username']
           password1 = dic['password']
           password2 = dic['password2']
           return HttpResponse(str(dic))
       else:
           return HttpResponse("表单验证失败")



