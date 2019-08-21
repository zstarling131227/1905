from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404


def index_view(request):
    return HttpResponse("主页")

def page1_view(request):
    raise Http404
    # return HttpResponse("页面1")


