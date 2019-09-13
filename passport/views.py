from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from main.utils import get_md5, generate_token
from passport.models import User


def login(request):
    context = {}
    context['msg_tips'] = '欢迎登录'
    context['bese_title'] = 'Login'
    user_md5 = request.session.get("user_md5")
    user_id = request.session.get("user_id")
    token=request.session.get("token")
    print("login", user_md5, user_id,token)

    return render(request, 'passport/login.html', context)


@csrf_exempt
def login_result(request):
    b = False
    if request.method == 'POST':
        username = request.POST.get('id_username')
        password = request.POST.get('id_password')
        user = User.objects.filter(account=username, pwd=get_md5(password))
        if user:
            user_md5 = get_md5(username)
            request.session["user_md5"] = user_md5
            request.session["user_id"] = user[0].id
            request.session["token"] = generate_token(user_md5)
            b = True

    if b:
        context = {}
        context['msg_tips'] = '登录成功'
        context['base_title'] = 'Login Result'
        return render(request, 'passport/login_result.html', context)
    else:
        context = {}
        context['msg_tips'] = '请重新登录'
        context['bese_title'] = 'Login'
        return render(request, 'passport/login.html', context)
