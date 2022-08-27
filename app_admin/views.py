from django.shortcuts import render,redirect
from blog.models import Document

def dashboard(request):
    #  if not request.user.is_authenticated:
    #   return redirect('home')
    return render(request,'db.html')


def user_documents(request):
    if not request.user.is_authenticated:
        return redirect('home')

    liste_documents=Document.objects.filter(user=request.user)
    return render(request,"mesdocuments.html",{'liste_documents':liste_documents})