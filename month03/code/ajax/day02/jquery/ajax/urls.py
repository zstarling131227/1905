from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^load_test/', views.load_test),
    url(r'^load_test_server/', views.load_test_server)
]
