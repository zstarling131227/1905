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
    url(r'^get_user/$', views.get_user, name='get_user'),
    url(r'^get_user_server/$', views.get_user_server, name='get_user_server'),
    url(r'^json_obj/$', views.json_obj, name='json_obj'),
    url(r'^json_dumps/$', views.json_dumps, name='json_dumps'),
]
