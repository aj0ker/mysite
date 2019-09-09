# _*_ coding: utf-8 _*_
#! /usr/bin/env python
# @Author   : aJ0ker
# @Time     : 2019/9/4 16:39
# @File     : urls.py

from django.urls import path
from . import views

app_name = 'aJ0ker'
urlpatterns = [
    path(r'',views.blog_list,name='blog_list'),
    path(r'<int:article_id>/',views.blog_detail,name='blog_detail'),
]