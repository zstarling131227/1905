from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^add$', views.new_book),
    url(r'^list_all', views.list_books),
    url(r'^mod/(\d+)$', views.mod_book_info),
    url(r'^del/(\d+)$', views.del_book),
    url(r'^title', views.title_book),
    url(r'^price', views.price_book),
    url(r'^down', views.down_book),
    url(r'^pub', views.not_pub),
    url(r'^search', views.search_book),
]
