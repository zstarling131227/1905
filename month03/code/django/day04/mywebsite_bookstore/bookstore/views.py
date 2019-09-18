from django.shortcuts import render
from django.http import HttpResponseRedirect  # 改入 HttpResponseRedirect模块用于 重定向url
from django.http import HttpResponse
from . import models


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def new_book(request):
    if request.method == 'GET':
        return render(request, 'new_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        pub_house = request.POST.get('pub_house', '')
        price = request.POST.get('price', '')
        market_price = request.POST.get('market_price', '')
        # 用Book.object管理器的create方法来创建新书
        abook = models.Book.objects.create(title=title,
                                           price=price,
                                           market_price=market_price,
                                           pub_house=pub_house)
        print('添加新书,成功添加新书:', abook.title)
        return HttpResponse('<a href="/bookstore">添加新书成功，点我跳转到首页</a>')


def list_books(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', locals())


def mod_book_info(request, book_id):
    # 先根据book_id 找到对应的一本书
    try:
        abook = models.Book.objects.get(id=book_id)
    except:
        return HttpResponse("没有找到ID为" + book_id + "的图书信息")

    if request.method == 'GET':
        return render(request, "mod_price.html", locals())
    elif request.method == 'POST':
        try:
            m_price = request.POST.get('market_price', '0.0')
            abook.market_price = m_price
            abook.save()  # 提交修改
            # return HttpResponse("修改成功")
            return HttpResponseRedirect('/bookstore/list_all')
        except:
            return HttpResponse("修改失败")


def del_book(request, book_id):
    try:
        abook = models.Book.objects.get(id=book_id)
        abook.delete()
        return HttpResponseRedirect('/bookstore/list_all')
    except:
        return HttpResponse("没有找到ID为" + book_id + "的图书信息,删除失败")


from django.db.models import Q
from django.db.models import F


# 1. 写一个页面，让用户输入输入一个价格，列出所有低于这个价格的图书（使用 `__lt`查询谓词)
# 2. 写一个页面，输入一个图书名字的一部分，列出所有包含此关键字的图书（使用`__contains`查询谓词)
# 3. 写一个页面来列出所有降价销售的图书(使用F()对象进行查询)
# 4. 写一个页面显示出不是"清华大学出版社" 且 价格小于50元的图书(提示: 使用Q()对象,~Q(pub_houst="清华大学出版社")&Q(price__lt=50))
def price_book(request):
    # for book in books:
    #     title = book.title
    #     price = book.price
    #     market_price = book.market_price
    #     pub_house = book.pub_house
    # return HttpResponse('price_book.html')
    if request.method == 'GET':
        return render(request, "price_book.html", locals())
    elif request.method == 'POST':
        try:
            price = request.POST.get('price', '0.0')
            books = models.Book.objects.filter(price__lt=price)
            print(books)
            if len(books) == 0:
                return HttpResponse("没有找到价格低于" + price + "的图书信息")
            else:
                return render(request, "price_book.html", locals())

        except Exception as err:
            return HttpResponse(err)


def title_book(request):
    # for book in books:
    #     title = book.title
    #     price = book.price
    #     pub_house = book.pub_house
    #     market_price = book.market_price
    # return HttpResponse('title_book.html')
    if request.method == 'GET':
        return render(request, "title_book.html", locals())
    elif request.method == 'POST':
        try:
            title = request.POST.get('title')
            books = models.Book.objects.filter(title__contains=title)
            if len(books):
                return render(request, "title_book.html", locals())
            else:
                return HttpResponse("没有找到含有" + title + "的图书信息")
        except Exception as err:
            return HttpResponse(err)


def down_book(request):
    try:
        books = models.Book.objects.filter(market_price__gt=F('price'))
    except:
        return HttpResponse("没有找到图书信息")
    # for book in books:
    #     # print(book.title, '定价:', book.price, '现价:', book.market_price)
    #     title=book.title
    #     price=book.price
    #     market_price=book.market_price
    #     pub_house = book.pub_house
    # return HttpResponse('down_book.html')
    if request.method == 'GET':
        return render(request, "down_book.html", locals())


def not_pub(request):
    try:
        books = models.Book.objects.filter(Q(price__lt=20) | Q(pub_house="清华大学出版社"))
    except:
        return HttpResponse("没有找到的图书信息")
    # for book in books:
    #     title = book.title
    #     price = book.price
    #     market_price = book.market_price
    #     pub_house = book.pub_house
    # return HttpResponse("not_pub.html")
    if request.method == 'GET':
        return render(request, "not_pub.html", locals())


def search_book(request):
    return render(request, 'search.html')
