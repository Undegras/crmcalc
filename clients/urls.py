from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='clients'),
    url(r'^clients/',views.index, name='clients'),
]