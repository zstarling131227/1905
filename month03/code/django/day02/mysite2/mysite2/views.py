# file :mysite2/views.py
from django.http import HttpResponse


def sum_view(request):
    ':<http://127.0.0.1:8000/sum?start=整数&stop=整数&step整数'
    if request.method == 'GET':
        try:
            start = request.GET.get('start', '0')
            start = int(start)
            stop = request.GET['stop']
            stop = int(stop)
            step = request.GET.get('step', 1)
            step = int(step)
            mysum = sum(range(start, stop, step))
            html = '和是：%d' % mysum
            return HttpResponse(html)
        except Exception:
            return HttpResponse('您给的查询字符串无效')


login_form_html = '''
<form action="/login" method="post">
    用户名：<input name="username" type="text">
    密  码：<input name="password" type="password">
    <input type="submit" value="登录">
</form>
'''


def login_view(request):
    if request.method == "GET":
        return HttpResponse(login_form_html)
    elif request.method == "POST":  # （补充）
        name = request.POST.get("username", '属性错误')
        html = "姓名：" + name
        # passwd = request.POST.get("password", '属性错误')
        # s = str(passwd)
        s = str(dict(request.POST))
        html += s
        return HttpResponse(html)


def login2_view(request):
    if request.method == "GET":
        '''
        #方法1：加载模板 用模板生成html 将HTML返回给浏览器
        from django.template import loader
        t=loader.get_template('mylogin.html')
        # render()括号中的值是填充到HTML中的value值，可以不填充，但是如果填充，只能是字典类型
        html=t.render({"name":'tarena'})
        return HttpResponse(html)
        '''
        # 方法2：
        from django.shortcuts import render
        return render(request, "mylogin.html", {"name": "王八蛋"})


def say_hello():
    return "hello!"

from django.shortcuts import render


def test_view(request):
    s = "Hello Tarena!"
    lst = ['北京', '上海', '重庆']
    mydic = {"name": 'tedu', "age": 20}
    dic = {"s": s, 'lst': lst, "mydic": mydic, "say_hello": say_hello()}
    return render(request, "test.html", dic)


def mytemp_view(request):
    # dic={
    #     "x":10
    # }
    x = 0
    return render(request, "mytemp.html", locals())


def mycal_view(request):
    if request.method=="GET":##要页面
        return render(request,"mycal.html")
    elif request.method=="POST":
        x=int(request.POST.get("x",'0'))
        y=int(request.POST.get("y",'0'))
        op=request.POST.get("op")
        if op=="add":
            result=x+y
        elif op=="sub":
            result=x-y
        elif op=="mul":
            result=x*y
        elif op=="div":
            result=x/y
        return render(request,"mycal.html",locals())


def for_view(request):
    s='WANGBAdan'
    w='<i>嘻嘻</i>'
    n=100
    lst=['北京','上海','天津','重庆']
    v="嘻 嘻 钥 玥 哈 哈"
    u="嘻嘻钥 玥哈哈"
    return render(request,"for.html",locals())


def index_view(request):
    return render(request,"base.html")

def sport_view(request):
    return render(request, "sport.html")

def new_view(request):
    return render(request, "new.html")

def pagen_view(request,n):
    return HttpResponse('第'+n +"页")