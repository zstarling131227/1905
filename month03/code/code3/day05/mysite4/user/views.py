from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def reg_view(request):
    if request.method == "GET":
        return render(request, "user/register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        passwd = request.POST.get("passwd")
        if passwd == password:
            try:
                models.User.objects.create(
                    username=username,
                    password=password,
                )
                resp = HttpResponse("添加成功")
                resp.set_cookie("user_register", username)
                return resp
            except Exception as err:
                return HttpResponse("添加失败")
        else:
            return HttpResponse("密码输入不一致")
