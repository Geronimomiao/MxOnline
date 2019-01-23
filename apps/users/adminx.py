# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx
   Description :
   Author :       wsm
   date：          2019-01-23
-------------------------------------------------
   Change Activity:
                   2019-01-23:
-------------------------------------------------
"""
__author__ = 'wsm'

import xadmin
from .models import EmailVerifyRecord, UserProfile, Banner


class EmailVerifyRecordAdmin(object):
    # 自定义 后台管理系统 显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索时 后台从 那些字段 进行搜索
    search_fields = ['code', 'email', 'send_type']
    # 配置 数据过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class UserProfileAdmin(object):
    list_display = ['nick_name', 'username', 'password', 'birthday', 'gender', 'address', 'mobile', 'image']
    search_fields = ['nick_name', 'username', 'password', 'gender', 'address', 'mobile', 'image']
    list_filter = ['nick_name', 'username', 'password', 'gender', 'address', 'mobile', 'image']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(Banner, BannerAdmin)