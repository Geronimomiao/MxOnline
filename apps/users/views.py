from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from apps.utils.email_send import send_register_email


# Create your views here.


class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
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
                if user.is_active:
                    # login 生成 session_id
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {"msg": "账号未激活"})
            else:
                return render(request, 'login.html', {"msg": "用户名或密码错误"})
        else:
            return render(request, 'login.html', {"msg": "用户名或密码错误"})


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            # 注册前 检测用户 是否存在
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {"register_form": register_form, "msg": '邮箱已被注册'})
            password = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = email
            user_profile.email = email
            user_profile.is_active = 0
            user_profile.password = make_password(password)
            user_profile.save()

            send_register_email(email, 'register')
            return render(request, 'send_success.html')
        else:
            # "register_form": register_form 为回填用户信息
            return render(request, 'register.html', {"register_form": register_form})


class ActiveUserView(View):

    def get(self, request, active_code):
        all_reconds = EmailVerifyRecord.objects.filter(code=active_code)
        if all_reconds:
            for recond in all_reconds:
                email = recond.email
                user = UserProfile.objects.get(email=email)
                user.is_active = 1
                user.save()
        else:
            # http://127.0.0.1:8000/active/sdfsdfwrgerg  防瞎输
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ForgetPwd(View):

    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", '')
            if UserProfile.objects.filter(email=email):
                send_register_email(email, 'forget')
                return render(request, 'send_success.html')
            else:
                return render(request, 'forgetpwd.html', {'forget_form': forget_form, "msg": '邮箱未被注册'})
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetView(View):
    #  urls.py 配置 必须传 active_code post 请求匹配不到
    def get(self, request, active_code):
        all_reconds = EmailVerifyRecord.objects.filter(code=active_code)
        if all_reconds:
            for recond in all_reconds:
                email = recond.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ModifyPwdView(View):

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {"email": email, 'msg': '密码不一致'})
            user_profile = UserProfile.objects.get(email=email)
            user_profile.password = make_password(pwd2)
            user_profile.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {"email": email, "modify_form": modify_form})

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
