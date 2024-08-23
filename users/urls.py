from django.urls import path
from .views import HomeView , register , login_user , logout_user

url_patterns = [
    path('' , HomeView.as_view() , name = 'home') ,
    path('register/' , register , name='register') ,
    path('login/' , login_user , name='login') ,
    path('logout/' , logout_user , name='logout') ,
]