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
from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    # 自定义 后台管理系统 显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
