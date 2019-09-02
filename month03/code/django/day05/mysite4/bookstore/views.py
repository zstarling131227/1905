from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models


# Create your views here.
def add_book(request):
    if request.method == 'GET':
        return render(request, "./bookstore/add_book.html")
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = float(request.POST.get('price', '0'))
        market_price = float(request.POST.get('market_price', '0'))
        try:
            models.Book.objects.create(
                title=title,
                price=price,
                pub=pub,
                market_price=market_price,
            )
            return HttpResponseRedirect("/bookstore/addbo")
        except Exception as err:
            return HttpResponse("添加失败")


def showbo_all(request):
    books = models.Book.objects.all()
    for abook in books:
        print("书名：" + abook.title)
    return HttpResponse("查询成功")


def addbo_view(request):
    books = models.Book.objects.all()
    return render(request, 'bookstore/addbo.html', locals())


def sel_one_book(request):
    ##price不能写price>50,否则会报错
    # books=models.Book.objects.filter(price=50)
    ##查询大于50的
    # books=models.Book.objects.filter(price__gt=50)
    # books=models.Book.objects.filter(price__range=(50,80))
    # books=models.Book.objects.filter(market_price__lt=50)
    # books=models.Book.objects.filter(pub__contains="清华大学")
    # books=models.Book.objects.filter(pub__endswith="出版社")
    # books = models.Book.objects.all()
    ##不包含括号内数据
    books = models.Book.objects.exclude(pub="清华大学出版社", price__gt=50)
    return render(request, 'bookstore/addbo.html', locals())


def modbo_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except Exception:
        return HttpResponse("没有id为" + id + "的数据记录")

    if request.method == 'GET':
        return render(request, 'bookstore/modbo.html', locals())
    elif request.method == "POST":
        market_price = float(request.POST.get('market_price', "0"))
        abook.market_price = market_price
        abook.save()
        ##绝对路径(跟的都是路由，并不是HTML的名字）
        return HttpResponseRedirect('/bookstore/addbo')
        # return HttpResponseRedirect('../addbo')


def delbo_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except Exception as err:
        return HttpResponse("删除失败")
    abook.delete()
    return HttpResponseRedirect("/bookstore/addbo")


def add_author(request):
    if request.method == 'GET':
        return render(request, "./bookstore/add_author.html")
    elif request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        try:
            models.Author.objects.create(
                name=name,
                age=age,
                email=email,
            )
            return HttpResponseRedirect("/bookstore/addau")
        except Exception as err:
            return HttpResponse("添加失败")


def showau_all(request):
    authors = models.Author.objects.all()
    for author in authors:
        print("作者：" + author.name)
    return HttpResponse("查询成功")


def addau_view(request):
    authors = models.Author.objects.all()
    return render(request, 'bookstore/addau.html', locals())


def sel_one_author(request):
    # authors=models.Author.objects.filter(age__gt=85)
    # authors=models.Author.objects.filter(name__startwith='王')
    authors = models.Author.objects.filter(email__contains='wc')
    return render(request, 'bookstore/addau.html', locals())


def modau_view(request, id):
    try:
        author = models.Author.objects.get(id=id)
    except Exception:
        return HttpResponse("没有id为" + id + "的数据记录")

    if request.method == 'GET':
        return render(request, 'bookstore/modau.html', locals())
    elif request.method == "POST":
        age = request.POST.get('age', "20")
        author.age = age
        author.save()
        return HttpResponseRedirect('/bookstore/addau')


def delau_view(request, id):
    try:
        author = models.Author.objects.get(id=id)
    except Exception as err:
        return HttpResponse("删除失败")
    author.delete()
    return HttpResponseRedirect("/bookstore/addau")


# cookie
def set_cookies_view(request):
    resp = HttpResponse("ok")
    resp.set_cookie("myvar", 300)
    # 10s之后cookie消失。
    # resp.set_cookie("myvar",300,max_age=10)
    # resp.set_cookie("myvar",300,max_age=10000000)
    # resp.delete_cookie('myvar')
    return resp


def get_cookies_view(request):
    v = request.COOKIES.get('myvar')
    return HttpResponse("myvar=" + v)
