from django.shortcuts import render
from . import models
from django.http import HttpResponse


# Create your views here.
def manytomany_init(request):
    author1 = models.Author3.objects.create(name="吕泽")
    author2 = models.Author3.objects.create(name="魏老师")
    book11 = author1.book3_set.create(title="Python")
    book21 = author1.book3_set.create(title="C++")
    book31 = author1.book3_set.create(title="C")
    author2.book3_set.add(book11)
    author2.book3_set.add(book21)
    return HttpResponse("初始化成功")


def show_manytomany(request):
    authors = models.Author3.objects.all()
    books = models.Book3.objects.all()
    for author in authors:
        print("作者：", author.name, "出版了", author.book3_set.count(), "本书")
        for book in books:
            print('    ', book.title)
    print("----显示书和作者的关系----")
    for book in books:
        auths = book.author.all()
        print(book.title, '的作者是:', '、'.join([str(x.name) for x in auths]))
    return HttpResponse("显示成功，请查看服务器端控制台终端")
