from unicodedata import name
from django.urls import path
from .views import *

urlpatterns=[
    path('login',login_toDoc,name='login'),
    path('register',register,name='register'),
    path('logout',logout_f,name='logout'),

    # admin
# 123456


]