### file :mysite1/views.py

from django.http import HttpResponse


def index_view(request):
    html = "<h1>这是我的首页</h1>"
    return HttpResponse(html)


def page1_view(request):
    html = "<h1>这是编号为1的网页</h1>"
    return HttpResponse(html)


def page2_view(request):
    html = "<h1>这是编号为2的网页</h1>"
    return HttpResponse(html)


def pagen_view(request, n):  # 此时的n是字符串类型，并非数值型
    html = "<h1>这是编号为%s的网页</h1>" % n
    return HttpResponse(html)


def math_view(request, x, op, y):
    x = int(x)
    y = int(y)
    result = None
    if op == 'add':
        result = x + y
    elif op == 'sub':
        result = x - y
    elif op == 'mul':
        result = x * y
    if result is None:
        return HttpResponse("出错了")
        # return HttpResponse("出错了")
    return HttpResponse("结果：" + str(result))


def person_view(request, name=None, age=None):
    s = "姓名：" + name
    s += "年龄：" + age
    return HttpResponse(s)


# def person_view(request,**kwargs):
#     s=str(kwargs)
#     return HttpResponse(s)

def birthday_view(request, y, m, d):
    html = "生日为：" + y + "年" + m + "月" + d + "日"
    return HttpResponse(html)


def birthday1_view(request, m, d, y):
    html = "生日为：" + y + "年" + m + "月" + d + "日"
    return HttpResponse(html)

def mypage_views(request):
    '''
    此视图函数用来示意得到的get请求中的查询参数
    http://127.0.0.1:8000/mypage?a=100&b=200
    '''
    if request.method == 'GET':
        # a = request.GET['a']  ##此时拿到是字符串
        # a = request.GET.get('a','没有对应的值')  ##此时拿到仍旧是字符串，且get不会报错，而且可以自己传参
        # html = "a=" + a
        a=request.GET.getlist('a')  ##['100']
        html = "a=" + str(a)
        b=request.GET.getlist('b')  ##['100']
        html = "b=" + str(b)
        # html = str(dict(request.GET))
        return HttpResponse(html)
    else:
        return HttpResponse('当前不是get请求')
