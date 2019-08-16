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


# 1. 写一个页面，让用户输入输入一个价格，列出所有低于这个价格的图书（使用 `__lt`查询谓词)
# 2. 写一个页面，输入一个图书名字的一部分，列出所有包含此关键字的图书（使用`__contains`查询谓词)
# 3. 写一个页面来列出所有降价销售的图书(使用F()对象进行查询)
# 4. 写一个页面显示出不是"清华大学出版社" 且 价格小于50元的图书(提示: 使用Q()对象,~Q(pub_houst="清华大学出版社")&Q(price__lt=50))