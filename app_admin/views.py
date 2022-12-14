
from ast import Return
from cgi import test

from inspect import Attribute
from pydoc import doc
from sre_constants import SUCCESS


from urllib import request
from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView , CreateView,DeleteView
from blog.models import Subcategorie, Document,Matiere,Institution, Année
from blog.forms import DocumentForm , SubcategorieForm ,SubcategorieForm1,MatiereForm,InstitutionForm,AnnéeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy , reverse
from blog.filters import DocumentFilter

def dashboard(request):
    #  if not request.user.is_authenticated:
    #   return redirect('login')
     liste_souscategorie=Subcategorie.objects.filter(user=request.user)
     return render(request,'db.html',{'liste_souscategorie':liste_souscategorie})

@login_required
def user_documents(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    liste_documents=Document.objects.filter(user=request.user)
    return render(request,'mesdocuments.html',{'liste_documents':liste_documents})



@login_required    
def user_institutions(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    liste_inst=Institution.objects.filter(user=request.user)
    return render(request,'inst.html',{'liste_inst':liste_inst})

    
@login_required    
def user_matiéres(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    liste_matieres=Matiere.objects.filter(user=request.user)
    return render(request,'matiéres.html',{'liste_matieres':liste_matieres})

@login_required    
def user_années(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    liste_années=Année.objects.filter(user=request.user)
    return render(request,'années.html',{'liste_années':liste_années})
   

      




@login_required
def Document_sous_category(request,chaine):

    # if not request.user.is_authenticated:
    #     return redirect('login')

   liste_documents=Document.objects.filter(user=request.user)
   liste_soucat=Subcategorie.objects.all()
    #tous les sous categorie
   if chaine:
         chaine=get_object_or_404(Subcategorie,titre_categorie=chaine)
         id = chaine.id
         liste_doc_soucat=liste_documents.filter(Subcategorie=chaine)
         liste_finale=liste_soucat.filter(parent=id)
        

   return render(request,'documents-souscat.html',{'liste_doc_soucat':liste_doc_soucat,'chaine':chaine,'liste_soucat':liste_soucat,'id':id,'liste_finale':liste_finale})




class addDocument(LoginRequiredMixin,CreateView,request.Request):
    model = Document
    form_class = DocumentForm
        
    template_name= "ajouter_document.html"

    #success_url="/my-admin/mes-documents" 
    # def get_success_url(self):
    #      return reverse_lazy('document_sous_category', kwargs={'soucat': self.object.Subcategorie})

    def get_success_url(self):
           
           return reverse("mes-documents")

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class addDocument1(LoginRequiredMixin,CreateView):
    
    model = Document
    form_class = DocumentForm
    template_name= "ajouter_document_selection.html"
    # matiéres=Document.objects.filter(user=request.user)

    # success_url="/my-admin/document_sous_category/TD"
    

    
    def get_success_url(self):
           # l'url ou je veux insérer le document (selon la souscatégorie ) subcategorie : un input trés important
           return reverse("document_sous_category", kwargs={'chaine':self.object.Subcategorie})
    # def get_success_url(self):
    #      return reverse_lazy('document_sous_category', kwargs={'soucat': self.object.Subcategorie})

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class addMatiére(LoginRequiredMixin,CreateView):
    
    model = Matiere
    form_class = MatiereForm
    template_name= "ajouter_matiére.html"

    # success_url="/my-admin/document_sous_category/TD"
    

    
    def get_success_url(self):
           # l'url ou je veux insérer le document (selon la souscatégorie ) subcategorie : un input trés important
           return reverse("Matiéres")
    # def get_success_url(self):
    #      return reverse_lazy('document_sous_category', kwargs={'soucat': self.object.Subcategorie})

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class addInstitution(LoginRequiredMixin,CreateView):
    
    model = Institution
    form_class = InstitutionForm
    template_name= "ajouter_institution.html"

    # success_url="/my-admin/document_sous_category/TD"
    def get_success_url(self):
           # l'url ou je veux insérer le document (selon la souscatégorie ) subcategorie : un input trés important
           return reverse("Institution")
    # def get_success_url(self):
    #      return reverse_lazy('document_sous_category', kwargs={'soucat': self.object.Subcategorie})

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class addAnnée(LoginRequiredMixin,CreateView):
    
    model = Année
    form_class = AnnéeForm
    template_name= "ajouter_année.html"

    # success_url="/my-admin/document_sous_category/TD"
    def get_success_url(self):
           # l'url ou je veux insérer le document (selon la souscatégorie ) subcategorie : un input trés important
           return reverse("Années")
    # def get_success_url(self):
    #      return reverse_lazy('document_sous_category', kwargs={'soucat': self.object.Subcategorie})

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

class UpdateDocument(LoginRequiredMixin,UpdateView ):
    model = Document
    form_class = DocumentForm
    template_name = 'app_admin/document_form.html'
    success_url= '/my-admin/mes-documents'
   

class DeleteDocument(LoginRequiredMixin,DeleteView):
    model = Document
    # form_class = DocumentForm
    template_name = 'app_admin/supprimer_form.html'
    # success_url= '/my-admin/mes-documents'
    def get_success_url(self):
        # obj=get_object_or_404(Subcategorie,titre_categorie=self.object.Subcategorie)
        # return reverse_lazy('document_sous_category', kwargs={'chaine': self.object.titre_categorie})
        return reverse_lazy('document_sous_category', kwargs={'chaine': self.object.Subcategorie})

    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('blog.supprimer-document'):
        #    raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class UpdateMatiére(LoginRequiredMixin,UpdateView):
    model = Matiere
    form_class = MatiereForm
    template_name = 'app_admin/matiére_form.html'
    success_url= '/my-admin/Matiéres'
   

class DeleteMatiére(LoginRequiredMixin,DeleteView):
    model = Matiere
    # form_class = DocumentForm
    template_name = 'app_admin/sup_matiére_form.html'
    success_url= '/my-admin/Matiéres'

    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('blog.supprimer-document'):
        #    raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class UpdateInstitution(LoginRequiredMixin,UpdateView):
    model = Institution
    form_class = InstitutionForm
    template_name = 'app_admin/institution_form.html'
    success_url= '/my-admin/Institution'
   

class DeleteInstitution(LoginRequiredMixin,DeleteView):
    model = Institution
    # form_class = DocumentForm
    template_name = 'app_admin/supprimer_institution.html'
    success_url= '/my-admin/Institution'

    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('blog.supprimer-document'):
        #    raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)    

class UpdateAnnée(LoginRequiredMixin,UpdateView):
    model = Année
    form_class = AnnéeForm
    template_name = 'app_admin/année_form.html'
    success_url= '/my-admin/Années'
   

class DeleteAnnée(LoginRequiredMixin,DeleteView):
    model = Année
    # form_class = DocumentForm
    template_name = 'app_admin/supprimer_année.html'
    success_url= '/my-admin/Années'

    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('blog.supprimer-document'):
        #    raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)        
    

class UpdateSouscategorie(LoginRequiredMixin,UpdateView):
    model = Subcategorie
    form_class = SubcategorieForm
    template_name = 'app_admin/soucategorie_form.html'
    # success_url: 'my-admin/'
    def get_success_url(self):
        if (self.object.parent is None):

          
            return reverse_lazy('dashboard') 
            

        obj=get_object_or_404(Subcategorie,titre_categorie=self.object.parent)
      
        
           
     
        return reverse_lazy('document_sous_category', kwargs={'chaine': obj.titre_categorie})
        
     
            
        

########################################################### ici un code important ######################
class DeleteSouscategorie(LoginRequiredMixin,DeleteView):
    model = Subcategorie
    # form_class = DocumentForm
    template_name = 'app_admin/supprimerSoucat_form.html'
    

    def get_success_url(self):
       
       
        if (self.object.parent is None):
            # obj=get_object_or_404(Subcategorie,titre_categorie=self.object.parent)
            Subcategorie.objects.filter(parent=self.object.id).delete()
            return reverse_lazy('dashboard') 
        # if (self.object.parent is not None):

        obj=get_object_or_404(Subcategorie,titre_categorie=self.object.parent)
        Subcategorie.objects.filter(parent=self.object.id).delete()
        return reverse_lazy('document_sous_category', kwargs={'chaine': obj.titre_categorie})


    # def get_success_url(self):
        
        # obj=get_object_or_404(Subcategorie,titre_categorie=self.object.parent)
        # # return reverse_lazy('document_sous_category', kwargs={'chaine': self.object.titre_categorie})
        # return reverse_lazy('document_sous_category', kwargs={'chaine': obj.titre_categorie})
    # success_url = reverse_lazy('document_sous_category',)
    # def get_absolute_url(self):

        # return reverse('document_sous_category', kwargs={'chaine':})

    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('blog.supprimer-document'):
        #    raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)    

####################################################################### fin code important #############

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
   
    def get_initial(self):
        
        return {
                 'parent':''
               }
    # def dispatch(self, request, *args, **kwargs):
    #     # if not request.user.has_perm('blog.supprimer-document'):
    #     #    raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)
    #success_url= "/my-admin/"

    def get_success_url(self):
           # l'url ou je veux insérer le document (selon la souscatégorie ) subcategorie : un input trés important
           return reverse("document_sous_category", kwargs={'chaine':self.object.parent})
  
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

   



#     def form_valid(self,form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

def test2(request,id) : 
    if request.method=="POST":
        
         user=request.user
         titre_categorie=request.POST['titre_categorie']
         desc=request.POST['desc']
         parent=request.POST['parent']
        #  parent_sub = Subcategorie.objects.filter(id=parent)
         obj=get_object_or_404(Subcategorie,id=parent)
        #  parent_sub_name = parent_sub.titre_categorie
         ins=Subcategorie(user=user,titre_categorie=titre_categorie,desc=desc,parent_id=parent)
         ins.save()
         return redirect('document_sous_category',chaine=obj.titre_categorie)
    
    return render(request,'ajouter_soucategorie1.html',{'id':id})  
  
     


       #  titre=request.POST['titre']
        #  description=request.POST['description']
        #  fichier= request.FILES.get('fichier')
        #  institution=request.POST['Institution']
        #  annee=request.POST['annee']
        #  matiére_name=request.POST['matiére_name']
        #  idsub=request.POST['Subcategorie']
        #  mat=Matiere.objects.get( matiére = matiére_name)
        #  sub=Subcategorie.objects.get( id = idsub)
        #  inst=Institution.objects.get( Institut = institution)
         
         
        #  ins=Document(user=mat.user,titre=titre,description=description,fichier=fichier,institution=inst,annee=annee,Subcategorie=sub,matiére=mat)
        #  ins.save()
       
          
    # return render(request,'ajouter_docu.html',{'id':id ,'liste_matieres':Matiere.objects.filter(user=request.user),'liste_insti_user':Institution.objects.filter(user=request.user)}) 
    
def ajout_document(request,id) : 
    bechnarja3=get_object_or_404(Subcategorie,id=id)





    ####################################danger#############################################
    form=DocumentForm(user=request.user) # rod balik tebadil minnou 7arf wa7id , RODBALI 
    ##########################################################################################


    annes_par_defaut= Année.objects.filter(user=request.user).last()
    matiere_par_defaut= Matiere.objects.filter(user=request.user).last()
    institut_par_defaut= Institution.objects.filter(user=request.user).last()
    # dossier_par_defaut = Subcategorie.objects.filter(id=id)
    obj=get_object_or_404(Subcategorie,id=id)
    form.fields['annee'].initial = annes_par_defaut
    form.fields['matiére'].initial = matiere_par_defaut
    form.fields['institution'].initial = institut_par_defaut
    form.fields['institution'].initial = institut_par_defaut
    form.fields['Subcategorie'].initial = obj

    if request.method=='POST':
        form = DocumentForm(request.user,request.POST,request.FILES)
        # form.user=request.user
        if form.is_valid():
             i=form.save(commit=False)
             ##########################
             i.user=request.user 
             ########################
             i.save()
             return redirect('mes-documents')

            #  return reverse_lazy('document_sous_category',kwargs={'chaine':bechnarja3.titre_categorie})

      
             
             
           
          
            
    # else:
    #      form = DocumentForm(user=request.user)
      
    return render(request,'ajouter_docu.html',{'id':id,'form':form , 'bechnarja3':bechnarja3}) 

def ajout_d(request) : 
 
    ####################################danger#############################################
    form=DocumentForm(user=request.user) # rod balik tebadil minnou 7arf wa7id , RODBALI 
    ##########################################################################################
    annes_par_defaut= Année.objects.filter(user=request.user).last()
    matiere_par_defaut= Matiere.objects.filter(user=request.user).last()
    institut_par_defaut= Institution.objects.filter(user=request.user).last()
    form.fields['annee'].initial = annes_par_defaut
    form.fields['matiére'].initial = matiere_par_defaut
    form.fields['institution'].initial = institut_par_defaut
    # form.fields['description'].initial = "ecrivez la description de votre document s'il vous plait"
   
    

    # form.fields['annee'].initial = get_object_or_404(Année,id=4)
    if request.method=='POST':
        form = DocumentForm(request.user,request.POST,request.FILES)
        # form.user=request.user
        if form.is_valid():
             i=form.save(commit=False)
             ##########################
             i.user=request.user 
             ########################
             i.save()
             return redirect('mes-documents')
            
    # else:
    #      form = DocumentForm(user=request.user)
      
    return render(request,'ajouter_docu1.html',{'form':form }) 


def modifier_docu(request,id) : 
    document=Document.objects.get(pk=id)
    ####################################danger#############################################
    form=DocumentForm(user=request.user,instance=document) # rod balik tebadil minnou 7arf wa7id , RODBALI 
    ##########################################################################################
    if request.method=='POST':
        form = DocumentForm(request.user,request.POST,request.FILES,instance=document)
        # form.user=request.user
        if form.is_valid():
             i=form.save(commit=False)
             ##########################
             i.user=request.user 
             ########################
             i.save()
             return redirect('mes-documents')
        
            
  
      
    return render(request,'modifier_docu.html',{'id':id,'form':form}) 


    
def modifier_document(request,id) : 


    document=Document.objects.get(pk=id)
    # document.titre = request.POST['titre']
   
    document.save(update_fields=['titre'])
    
    


  
         
    
         
       
    
    return render(request,'modifier_docu.html',{'document':document,'id':id ,'liste_matieres':Matiere.objects.filter(user=request.user),'liste_insti_user':Institution.objects.filter(user=request.user)}) 
    
    

       
def rechercher_document(request):
    form=DocumentForm(user=request.user)
    documents=Document.objects.filter(user=request.user)
    # status_filter = status_list.filter(user=request.user)
    # MyFilter= DocumentFilter(request.GET,queryset=documents)
    MyFilter= DocumentFilter(request.GET,queryset=documents)
    documents=MyFilter.qs
 
    

   
    return render(request,"rechercher.html",{'MyFilter':MyFilter,'documents':documents})


    
      

         