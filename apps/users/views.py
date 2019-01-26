from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile
from .forms import LoginForm, RegisterForm
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 通过类的方法 验证用户是否登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                request,
                username=request.POST.get('username', ''),
                password=request.POST.get('password', '')
            )
            if user is not None:
                # login 生成 session_id
                login(request, user)
                return render(request, 'index.html')
        else:
            return render(request, 'login.html', {"msg": "用户名或密码错误"})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
    def post(self, request):
        pass

# # 通过函数方法 验证用户是否登录
# def user_login(request):
#     if request.method == 'POST':
#         # 根据 settings.py AUTHENTICATION_BACKENDS 字段里确定
#         user = authenticate(
#             request,
#             username=request.POST.get('username', ''),
#             password=request.POST.get('password', '')
#         )
#         if user is not None:
#             login(request, user)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html', {"msg": "用户名或密码错误"})
#     elif request.method == 'GET':
#         # render 第一个参数 request 第二个参数 模版名 第三个参数 模版需要等变量
#         return render(request, 'login.html', {})