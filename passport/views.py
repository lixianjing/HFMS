from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from main.user_utils import get_id
from main.utils import get_md5, generate_token, certify_token
from passport.models import User, UserGroup


def login(request):
    context = {}
    user_id = request.session.get("user_id")
    token = request.session.get("token")
    if bool(user_id) & bool(token):
        if certify_token(user_id, token):
            context['msg_tips'] = '登录成功'
            context['bese_title'] = '个人中心'
            return render(request, 'passport/user_center.html', context)
        else:
            context['msg_tips'] = '登录过期，重新登录'
    else:
        context['msg_tips'] = '欢迎登录'
    request.session.clear()
    context['bese_title'] = 'Login'
    return render(request, 'passport/login.html', context)


@csrf_exempt
def login_result(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('id_username')
        password = request.POST.get('id_password')
        user = User.objects.filter(account=username, pwd=get_md5(password))
        if user:
            request.session["user_id"] = str(user[0].id)
            request.session["token"] = generate_token(str(user[0].id))
            context['msg_tips'] = '登录成功'
            context['base_title'] = '个人中心'
            context['user']=user
            return render(request, 'passport/user_center.html', context)
        else:
            context['msg_tips'] = '登录失败，没有该用户'
    else:
        context['msg_tips'] = '请求失败，请重试'
    context['bese_title'] = 'Login'
    return render(request, 'passport/login.html', context)



def regist(request):
    context = {}
    context['msg_tips'] = '用户注册'
    context['bese_title'] = '注册'
    context['groups'] = UserGroup.objects.order_by("id")
    return render(request, 'passport/page_regist.html', context)


@csrf_exempt
def action_regist(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('id_username')
        password = request.POST.get('id_password')
        nick = request.POST.get('id_nick')
        phone = request.POST.get('id_phone')
        sex = request.POST.get('id_sex')
        group_id = request.POST.get('id_group')
        print(username, password, nick, phone, sex)
        if bool(username) & bool(password) & bool(nick) & bool(phone) & bool(sex) & bool(group_id):
            try:
                id = get_id()
                user = User(id=id, account=username, pwd=password, nick_name=nick, phone=phone, sex=sex,
                            group_id=group_id)
                user.save()
                request.session["user_id"] = str(id)
                request.session["token"] = generate_token(str(id))
                context['msg_tips'] = '注册成功'
                context['base_title'] = '个人中心'
                context['user'] = user
                return render(request, 'passport/user_center.html', context)
            except Exception as err:
                print('err:', err)
                context['msg_tips'] = '数据库错误，请重试'
        else:
            context['msg_tips'] = '信息不全，请重试'
    else:
        context['msg_tips'] = '请求失败，请重试'
    context['bese_title'] = '注册'
    return render(request, 'passport/page_regist.html', context)
