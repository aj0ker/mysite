# _*_ coding: utf-8 _*_
#! /usr/bin/env python
# @Author   : aJ0ker
# @Time     : 2019/9/5 16:46
# @File     : forms.py

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)