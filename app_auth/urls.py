from unicodedata import name
from django.urls import path
from .views import login

urlpatterns=[
    path('login',login,name='login')

    # admin
# 123456


]