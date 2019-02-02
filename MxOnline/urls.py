"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
from django.views.generic import TemplateView


# from users.views import user_login
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwd, ResetView, ModifyPwdView
from django.views.static import serve
from . import settings
import organization

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),

    # 从 url 中提取参数
    re_path(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),

    re_path(r'^forget/', ForgetPwd.as_view(), name='forget_pwd'),
    re_path(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    re_path(r'^modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),

    # 课程机构 url 配置
    re_path(r'^org/', include(('organization.urls', 'organization'), namespace='org')),

    # 配置上传文件的访问处理函数
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
