from django.shortcuts import render
from django.http import HttpResponse
from . import  models
# Create your views here.
def add_view(request):
    try:
        ##方法1：
        abook=models.Book.objects.create(
            title='C++',price=68)
        ##方法2：
        # abook=models.Book(price=98)
        # abook.title="西游记"
        # abook.save()
        return HttpResponse("添加图书成功")
    except Exception as err:
        return  HttpResponse("添加图书失败")