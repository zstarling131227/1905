from django.conf.urls import url
from . import views

##urlpatterns名称跟主路由的名字urlpatterns必须一样
urlpatterns = [
    url(r'^$', views.index_view),
]