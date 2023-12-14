from django.urls import path
from User.views import *
from . import views

app_name = 'User'

urlpatterns = [
        path("register/",views.register,name="register"),
        path("login/",views.login,name="login"),
]
