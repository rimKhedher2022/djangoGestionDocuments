
from inspect import Attribute
from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView , CreateView,DeleteView
from blog.models import Subcategorie, Document
from blog.forms import DocumentForm , SubcategorieForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

def dashboard(request):
     if not request.user.is_authenticated:
      return redirect('login')
     liste_souscategorie=Subcategorie.objects.all()
     return render(request,'db.html',{'liste_souscategorie':liste_souscategorie})

@login_required
def user_documents(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    liste_documents=Document.objects.filter(user=request.user)
    return render(request,'mesdocuments.html',{'liste_documents':liste_documents})

@login_required
def Document_sous_category(request,soucat):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    liste_documents=Document.objects.filter(user=request.user)
    liste_souscategorie=Subcategorie.objects.all() #tous les sous categorie
    if soucat:
         soucat=get_object_or_404(Subcategorie,titre_categorie=soucat)
         liste_documents_scat=liste_documents.filter(Subcategorie=soucat)

    return render(request,'documents-souscat.html',{'liste_documents_scat':liste_documents_scat})









class addDocument(LoginRequiredMixin,CreateView):
    model = Document
    form_class = DocumentForm
    template_name= "ajouter_document.html"
    # success_url="/my-admin/document_sous_category/{% Document. %}" 
    def get_success_url(self):
         return reverse_lazy('document_sous_category', kwargs={'soucat': self.object.Subcategorie})
      
   


    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateDocument(LoginRequiredMixin,UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'app_admin/document_form.html'
    success_url= '/my-admin/mes-documents'
   

class DeleteDocument(LoginRequiredMixin,DeleteView):
    model = Document
    # form_class = DocumentForm
    template_name = 'app_admin/supprimer_form.html'
    success_url= '/my-admin/mes-documents'

    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('blog.supprimer-document'):
        #    raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class UpdateSouscategorie(LoginRequiredMixin,UpdateView):
    model = Subcategorie
    form_class = SubcategorieForm
    template_name = 'app_admin/soucategorie_form.html'
    success_url= '/my-admin'

class DeleteSouscategorie(LoginRequiredMixin,DeleteView):
    model = Subcategorie
    # form_class = DocumentForm
    template_name = 'app_admin/supprimerSoucat_form.html'
    success_url= '/my-admin'

    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('blog.supprimer-document'):
        #    raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)    



class addSouscategorie(LoginRequiredMixin,CreateView):
    model = Subcategorie
    form_class = SubcategorieForm
    template_name= "ajouter_soucategorie.html"
    success_url= '/my-admin'
   


    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)        