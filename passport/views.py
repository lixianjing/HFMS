from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def login(request):
    context = {}
    context['msg_tips'] = '欢迎登录'
    context['bese_title'] = 'Login'
    return render(request, 'passport/login.html', context)


@csrf_exempt
def login_result(request):
    b = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'lmf':
            b = True

    print("username:" + username + ",password:" + password)
    # return HttpResponse("Hello world ! "  + ":" )

    # user = User.objects.filter(username=username, password=my_md5(password))
    # if user:
    #     # 将用户的username保存到session中
    #     request.session["login_user"] = username

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
