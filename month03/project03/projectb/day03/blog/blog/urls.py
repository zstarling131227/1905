"""blog URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^test/$', views.test_api)时，输入http://127.0.0.1:8000/test会自动补入/(前提是你有一个带/的路由),关闭方法为在setting中添加APPEND_SLASH =
    # False。此时输入http://127.0.0.1:8000/test没有页面存在时会报错。
    url(r'^test/$', views.test_api),
    # http://127.0.0.1:8000/v1/users
    url(r'^v1/users', include('user.urls')),
    # http://127.0.0.1:8000/v1/tokens
    url(r'^v1/tokens', include('btoken.urls')),

]
