
from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView , CreateView,DeleteView
from blog.models import Document
from blog.forms import DocumentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms


def dashboard(request):
    #  if not request.user.is_authenticated:
    #   return redirect('home')
    return render(request,'db.html')


def user_documents(request):
    if not request.user.is_authenticated:
        return redirect('home')

    liste_documents=Document.objects.filter(user=request.user)
    return render(request,'mesdocuments.html',{'liste_documents':liste_documents})




class addDocument(CreateView):
    model = Document
    form_class = DocumentForm
    template_name= "ajouter_document.html"
    success_url="mes-documents" 


    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    


 