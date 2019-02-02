# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :       wsm
   date：          19-2-2
-------------------------------------------------
   Change Activity:
                   19-2-2:
-------------------------------------------------
"""
__author__ = 'wsm'

from django.urls import path, include, re_path
from .views import OrgView, AddUserAskView

urlpatterns = [
    # 课程机构首页
    re_path(r'^list/$', OrgView.as_view(), name='org_list'),
    re_path(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
]