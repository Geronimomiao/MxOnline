# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     forms
   Description :
   Author :       wsm
   date：          19-2-2
-------------------------------------------------
   Change Activity:
                   19-2-2:
-------------------------------------------------
"""
__author__ = 'wsm'

# from django import forms
#
# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     phone = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, min_length=1, max_length=50)
import re

from django import forms
from operation.models import UserAsk

class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        # 验证手机号码是否合法
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[34578]\d{9}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code='mobile_invalid')

