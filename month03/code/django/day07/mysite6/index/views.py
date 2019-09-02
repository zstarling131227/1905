from django.shortcuts import render
import os
from mysite6 import settings
# Create your views here.
# file: index/views.py

def index_view(request):
    return render(request, 'index/index.html', locals() )

from django.http import HttpResponse

def test_view(request):
    print('test_view被调用！')
    return HttpResponse("请求到达了/test页面")

def upload_view(request):
    if request.method=='GET':
        return render(request,'index/upload.html')
    elif request.method=='POST':
        a_file=request.FILES['myfile']
        print("收到上传的文件：",a_file.name)
        filename=os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(filename,'wb') as fw:
            fw.write(a_file.file.read())
        return HttpResponse("上传文件"+a_file.name)
    return HttpResponse('上传失败')
