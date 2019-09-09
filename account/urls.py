# _*_ coding: utf-8 _*_
#! /usr/bin/env python
# @Author   : aJ0ker
# @Time     : 2019/9/5 16:58
# @File     : urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    #path(r'login/',views.user_login,name='user_login'),
    path(r'login/',auth_views.LoginView.as_view(template_name='account/login.html'),name='user_login'),     #使用Django内置的登录方法
    path(r'loginout/',auth_views.LogoutView.as_view(template_name='account/logout.html'),name='user_logout'),       #使用Django内置的登出方法
]