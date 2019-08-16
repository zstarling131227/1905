from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^add_book',views.add_book),
    url(r'^add_author',views.add_author),
    url(r'^allbo',views.showbo_all),
    url(r'^allau',views.showau_all),
    url(r'^addbo$',views.addbo_view),
    url(r'^addau$',views.addau_view),
    url(r'^selbo',views.sel_one_book),
    url(r'^selau',views.sel_one_author),
    url(r'^modbo/(\d+)',views.modbo_view),
    url(r'^modau/(\d+)',views.modau_view),
    url(r'^delbo/(\d+)',views.delbo_view),
    url(r'^delau/(\d+)',views.delau_view),
    url(r'^set',views.set_cookies_view),
    url(r'^get',views.get_cookies_view),
]