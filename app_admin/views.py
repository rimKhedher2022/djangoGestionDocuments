
from inspect import Attribute
from urllib import request
from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView , CreateView,DeleteView
from blog.models import Subcategorie, Document
from blog.forms import DocumentForm , SubcategorieForm ,SubcategorieForm1
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy , reverse

def dashboard(request):
    #  if not request.user.is_authenticated:
    #   return redirect('login')
     liste_souscategorie=Subcategorie.objects.all()
     return render(request,'db.html',{'liste_souscategorie':liste_souscategorie})

@login_required
def user_documents(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    liste_documents=Document.objects.filter(user=request.user)
    return render(request,'mesdocuments.html',{'liste_documents':liste_documents})

@login_required
def Document_sous_category(request,chaine):

    # if not request.user.is_authenticated:
    #     return redirect('login')

   liste_documents=Document.objects.filter(user=request.user)
   liste_soucat=Subcategorie.objects.all() #tous les sous categorie
   if chaine:
         chaine=get_object_or_404(Subcategorie,titre_categorie=chaine)
         id = chaine.id
         liste_doc_soucat=liste_documents.filter(Subcategorie=chaine)
        

   return render(request,'documents-souscat.html',{'liste_doc_soucat':liste_doc_soucat,'chaine':chaine,'liste_soucat':liste_soucat,'id':id})









class addDocument(LoginRequiredMixin,CreateView):
    model = Document
    form_class = DocumentForm
    template_name= "ajouter_document.html"

    #success_url="/my-admin/mes-documents" 
    # def get_success_url(self):
    #      return reverse_lazy('document_sous_category', kwargs={'soucat': self.object.Subcategorie})

    def get_success_url(self):
           
           return reverse("document_sous_category", kwargs={'chaine':'TD'})

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class addDocument1(LoginRequiredMixin,CreateView):
    
    model = Document
    form_class = DocumentForm
    template_name= "ajouter_document.html"

    # success_url="/my-admin/document_sous_category/TD"
    

    
    def get_success_url(self):
           # l'url ou je veux insérer le document (selon la souscatégorie ) subcategorie : un input trés important
           return reverse("document_sous_category", kwargs={'chaine':self.object.Subcategorie})
    # def get_success_url(self):
    #      return reverse_lazy('document_sous_category', kwargs={'soucat': self.object.Subcategorie})

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
    
   # 
   # if (model.parent is not None):
    #     def get_success_url(self):
    #         return reverse_lazy('document_sous_category', kwargs={'soucat':Subcategorie})
    # else :
    success_url= "/my-admin/"
   



    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)    


class test1(LoginRequiredMixin,CreateView,request.Request):
    model = Subcategorie
    form_class = SubcategorieForm1
    template_name= "ajouter_soucategorie1.html"
    # def dispatch(self, request, *args, **kwargs):
    #     # if not request.user.has_perm('blog.supprimer-document'):
    #     #    raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)
    #success_url= "/my-admin/"

    def get_success_url(self):
           # l'url ou je veux insérer le document (selon la souscatégorie ) subcategorie : un input trés important
           return reverse("document_sous_category", kwargs={'chaine':self.object.parent})
   # 
   # if (model.parent is not None):
    #     def get_success_url(self):
    #         return reverse_lazy('document_sous_category', kwargs={'soucat':Subcategorie})
    # else :
    
   



#     def form_valid(self,form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

def test2(request,chaine) : 
    if request.method=="POST":
        titre=request.POST['titre']
        fichier=request.POST['fichier']
        institution=request.POST['institution']
        annee=request.POST['annee']
        matiére=request.POST['matiére']
        Subcategorie=request.POST['matiére']
        description=request.POST['description']
        # print(titre,institution,annee,matiére,Subcategorie,description)
        ins=Document(titre=titre,fichier=fichier,institution=institution,annee=annee,matiére=matiére,Subcategorie=Subcategorie,description=description)
        ins.save()
        print('ok')

    print(chaine) 
    return render(request,'test.html',{'chaine':chaine })  
    # teraja3 el kilma fil URL (exemple TD)  
    
    

       



    
      

         