from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^many',views.manytomany_init),
    url(r'^show',views.show_manytomany),
]