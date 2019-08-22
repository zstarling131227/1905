from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^xhr/$', views.xhr, name='xhr'),
    url(r'^get-xhr/$', views.get_xhr, name='get_xhr'),
    url(r'^get-xhr-server/$', views.get_xhr_server, name='get_xhr_server'),
    url(r'^register/$', views.register, name='register'),
    url(r'^checkuname/$', views.checkuname, name='checkuname'),
    url(r'^make_post/$', views.make_post, name='make_post'),
    url(r'^make1_post/$', views.make1_post, name='make1_post'),
]
