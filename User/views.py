from django.shortcuts import render
from django.http import HttpResponse
from productApp89.models import Product
from django.core.exceptions import MultipleObjectsReturned

# Create your views here.

from User.models import User


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not username:
            return HttpResponse("用户名不能为空")
        if not email:
            return HttpResponse("邮箱不能为空")
        if not password:
            return HttpResponse("密码不能为空")

        user = User(username=username, email=email, password=password)
        user.save()
        return render(request, 'home.html')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not username:
            return HttpResponse("用户名不能为空")
        if not email:
            return HttpResponse("邮箱不能为空")
        if not password:
            return HttpResponse("密码不能为空")
        
        try:
            user = User.objects.get(email=email)
            if password == user.password:
                return render(request, 'home.html')
            else:
                return HttpResponse('登录失败')
        except User.DoesNotExist:
            return HttpResponse('用户不存在')
        except MultipleObjectsReturned:
            return HttpResponse('存在多个匹配的用户，请联系管理员处理')
    return render(request, 'login.html')
