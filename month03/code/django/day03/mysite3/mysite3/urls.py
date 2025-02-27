"""mysite3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
# 子路由时使用
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shebao', views.shebao_view),
    # import music.views
    # 同一个app太多路由时，创建自子路由urls.py
    # url(r'^music/page1', music.views.page1_view),
    # url(r'^music/page2', music.views.page2_view),
    # url(r'^music/page3', music.views.page3_view),

    url(r'music/',include('music.urls')),
    url(r'index/',include('index.urls')),
    url(r'sport/',include('sport.urls')),
    url(r'news/',include('news.urls')),
    url(r'bookstore/',include('bookstore.urls')),
]
