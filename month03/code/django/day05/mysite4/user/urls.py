from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reg', views.reg_view),
]
