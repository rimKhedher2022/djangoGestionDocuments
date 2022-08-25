from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages

def login(request):  

    # admin
# 123456                        
    if request.method == "POST":
        username1=request.POST['username1']
        pwd=request.POST['pwd']
        user=authenticate(username=username1,password=pwd)
        if user is not None:
            
                return redirect("home")
        else:
                messages.error(request,"Erreur d'authentification")
                return render(request,"login.html")

# admin
# 123456

    return render(request,"login.html")
