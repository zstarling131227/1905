from django.conf.urls import url
from . import views

urlpatterns = [
    ##主路由末尾不带/，此时为http://127.0.0.1:8000/v1/users
    ##主路由末尾带/，此时为http://127.0.0.1:8000/v1/users/(django默认为带/型的)

    # http://127.0.0.1:8000/v1/users
    url(r'^$', views.users),
    # http://127.0.0.1:8000/v1/users/<username>
    # #绑定一个函数
    url(r'^/(?P<username>[\w]{1,11})$', views.users),
    # #单独使用两个函数
    # url(r'^/(?P<username>[\w]{1,11})$', views.users1),
    # url(r'^/(?P<username>[\w]{1,11})$', views.users_detail),
]
