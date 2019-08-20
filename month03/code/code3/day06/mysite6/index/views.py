from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    return render(request,'index/index.html',locals())


def test_view(request):
    return HttpResponse("被钓鱼")
    # return HttpResponse("被钓鱼")
    # return HttpResponse("被钓鱼")