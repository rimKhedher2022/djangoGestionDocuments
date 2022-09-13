from ast import keyword
from multiprocessing import context
from pydoc import doc
from turtle import title
from django.shortcuts import render
from .models import Document
import PyPDF2
import fitz
import os
from django.core.files.storage import default_storage

def home(request):
    
    list_documents=Document.objects.filter(user=request.user)
    context={"liste_documents":list_documents}
 
    return render(request,"index.html",context)



def detail(request,id_document):
    document=Document.objects.get(id=id_document)
    Subcategorie=document.Subcategorie
    documents_en_relations = Document.objects.filter(Subcategorie=Subcategorie)
   
    return render(request,"detail.html",{"document":document,"der":documents_en_relations,'Subcategorie':Subcategorie})



def document_detail(request,id_document):

    document=Document.objects.get(id=id_document)
    documents_dans_palteforme = Document.objects.filter(user=request.user)
    return render(request,"detail2.html",{"document":document,"der":documents_dans_palteforme})
    
# def look(fichier,word):
        
    
           

def search(request):
    query=request.GET["document"] 
    # la valeur qui peut etre un mot (ex:café) ==> query
    
   # file1=open(f.fichier.path,"r",encoding="latin-1")
        # if query in file1.read():
        #     print("true")

    liste_document_search=Document.objects.filter(titre__icontains=query) 
    
    return render(request,"search.html",{"liste_document_search":liste_document_search})
    

