# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     forms
   Description :    对用户提交对表单信息 做各种检测
   Author :       wsm
   date：          2019-01-25
-------------------------------------------------
   Change Activity:
                   2019-01-25:
-------------------------------------------------
"""
__author__ = 'wsm'

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # required=True 若字段为空 则会报错
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # error_messages 定制 遇到异常 抛出的报错信息
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

