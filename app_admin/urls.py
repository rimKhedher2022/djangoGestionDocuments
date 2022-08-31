import imp
from django.urls import path
from .views import *

urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('mes-documents',user_documents,name="mes-documents"),
     path('ajouter-document',addDocument.as_view(),name="ajouter-document"),
     ####################################################################################
    path('ajouter-document1/<str:chaine>',addDocument1.as_view(),name="ajouter-document1"),  
    ###################################################################################
    path('modifier-document/<int:pk>',UpdateDocument.as_view(),name="modifier-document"),
    path('supprimer-document/<int:pk>',DeleteDocument.as_view(),name="supprimer-document"),
   
    path('modifier-souscategorie/<int:pk>',UpdateSouscategorie.as_view(),name="modifier-souscategorie"),
    path('supprimer-souscategorie/<int:pk>',DeleteSouscategorie.as_view(),name="supprimer-souscategorie"),
    path('ajouter-souscategorie',addSouscategorie.as_view(),name="ajouter-souscategorie"),
     path('document_sous_category/<str:chaine>',Document_sous_category,name="document_sous_category"),
     path('document_sous_category/<int:chaine>',Document_sous_category,name="document_sous_category"),
     ################################################################################################
    path('ajouter-soucategorie1/<int:id>',test1.as_view(),name="ajouter-souscategorie1"),
    #####################################################################################################
    path('ajouter-un-document/<str:chaine>',test2,name="ajouter"),
]
