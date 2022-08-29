from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *


def login_toDoc(request):  

            # admin
            # 123456                        
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"Authentification échouée")
                return render(request,'login.html',{'form':form})    
        else :
            for field in form.errors:
             form[field].field.widget.attrs['class']+= ' is-invalid'
            return render(request,'login.html',{'form':form})


    else:
        form=LoginForm()

    return render(request,"login.html",{'form':form})


                # admin
                # 123456


def register(request):
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            pwd=form.cleaned_data["pwd"]
            user = User.objects.create_user(username=username,password=pwd)
            if user is not None:
                return redirect("login")
            else:
                messages.error(request,"création de compte échouée") 
                return render(request,'register.html',{'form':form})   
        else:
            return render(request,'register.html',{'form':form})
            return render(request,"register.html",{})
    else:
  
        
        form = RegisterForm()
        return render(request,"register.html",{'form':form}) 




def logout_f(request):
        logout(request)
        return redirect('login')
