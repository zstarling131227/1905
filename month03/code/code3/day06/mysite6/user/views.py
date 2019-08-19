from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
def reg_view(request):
    if request.method == "GET":
        # dic = request.COOKIES.get()
        # print("COOKIES=", dic)
        return render(request, "user/register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        passwd = request.POST.get("passwd")
        if len(username) < 6:
            username_error = '用户名太短'
            return render(request, 'user/register.html', locals())
        if len(password)==0:
            password_error="密码不能为空"
            return render(request, 'user/register.html', locals())
        if passwd == password:
            try:
                models.User.objects.create(
                    username=username,
                    password=password,
                )
                html='''
                注册成功<a href="/user/login">点击登录</a>
                '''
                resp = HttpResponse(html)
                resp.set_cookie("user_register", username)
                return resp
            except Exception as err:
                # return HttpResponse(err)
                # return HttpResponse('用户名已存在')
                username_error = '用户名已存在'
                return render(request, 'user/register.html', locals())
        else:
            return HttpResponse("密码输入不一致")

def login_view(request):
    # request.session['abc']=123
    # val=request.session.get('abc','xxx')
    # print('val=',val)
    # return HttpResponse('ok')
    if request.method == "GET":
        username = request.COOKIES.get('username','')
        print("COOKIES=", username)
        return render(request, "user/login.html",locals())
    elif request.method == "POST":
        username = request.POST.get("username",'')
        password = request.POST.get("password",'')
        if username == '':
            username_error='用户名不能为空'
            return render(request,'user/login.html',locals())
        try:
            auser=models.User.objects.get(username=username,password=password)
            request.session['user']={
                'username':username,
                'id':auser.id
            }
            resp = HttpResponseRedirect('/')
            if 'remember' in request.POST:
                resp.set_cookie('username',username)
            return resp
            # return HttpResponse('登录成功')
        except Exception as err:
            password_error='用户名或密码错误'
            return render(request,'user/login.html',locals())

def logout_view(request):
    if 'user' in request.session:
        del request.session['user']
    return HttpResponseRedirect('/')
