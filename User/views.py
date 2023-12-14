from django.shortcuts import render
from django.http import HttpResponse
from productApp89.models import Product
from productApp89.models import ProductImg
# Create your views here.

from User.models import User


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User()
        user.username = username
        user.email = email
        user.password = password
        user.save()
    return render(request,'register.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        if password == user.password:
            return render(request,'home.html')
        else:
            return HttpResponse('登录失败')
    return render(request,'login.html')
