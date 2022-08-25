from multiprocessing import context
from pydoc import doc
from turtle import title
from django.shortcuts import render
from .models import Document


def home(request):
    list_documents=Document.objects.all()
    context={"liste_documents":list_documents}
 
    return render(request,"index.html",context)



def detail(request,id_document):
    document=Document.objects.get(id=id_document)
    categorie=document.categorie
    documents_en_relations= Document.objects.filter(categorie=categorie)
   
    return render(request,"detail.html",{"document":document,"der":documents_en_relations})

def search(request):
    query=request.GET["document"] 
    # la valeur qui peut etre un mot (ex:café) ==> query
    liste_document_search=Document.objects.filter(titre__icontains=query) or Document.objects.filter(description__contains=query)
    return render(request,"search.html",{"liste_document_search":liste_document_search})
   