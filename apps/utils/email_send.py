# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     email_send
   Description :
   Author :       wsm
   date：          2019-01-26
-------------------------------------------------
   Change Activity:
                   2019-01-26:
-------------------------------------------------
"""
__author__ = 'wsm'

from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    # 可选字符
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '慕学在线网 注册激活链接'
        email_body = '请点击下面对链接 激活你的账号: http://127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

        if send_status:
            pass