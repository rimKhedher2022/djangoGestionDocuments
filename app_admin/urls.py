import imp
from django.urls import path
from .views import *

urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('mes-documents',user_documents,name="mes-documents"),
    path('Institution',user_institutions,name="Institution"),
    path('Matiéres',user_matiéres,name="Matiéres"),
    path('ajouter-document',addDocument.as_view(),name="ajouter-document"),
    path('ajouter-matiére',addMatiére.as_view(),name="ajouter-matiére"),
    path('ajouter-institution',addInstitution.as_view(),name="ajouter-institution"),
     ####################################################################################
    path('ajouter-document1/<str:chaine>',addDocument1.as_view(),name="ajouter_document_selection"),  
    ###################################################################################
    path('modifier-document/<int:pk>',UpdateDocument.as_view(),name="modifier-document"),
    path('supprimer-document/<int:pk>',DeleteDocument.as_view(),name="supprimer-document"),
   
    path('modifier-matiére/<int:pk>',UpdateMatiére.as_view(),name="modifier-matiere"),
    path('supprimer-matiére/<int:pk>',DeleteMatiére.as_view(),name="supprimer-matiere"),

    path('modifier-institution/<int:pk>',UpdateInstitution.as_view(),name="modifier-institution"),
    path('supprimer-institution/<int:pk>',DeleteInstitution.as_view(),name="supprimer-institution"),
   
    path('modifier-souscategorie/<int:pk>',UpdateSouscategorie.as_view(),name="modifier-souscategorie"),
    path('supprimer-souscategorie/<int:pk>',DeleteSouscategorie.as_view(),name="supprimer-souscategorie"),
    path('ajouter-souscategorie',addSouscategorie.as_view(),name="ajouter-souscategorie"),
     path('document_sous_category/<str:chaine>',Document_sous_category,name="document_sous_category"),
    #path('document_sous_category/<int:chaine>',Document_sous_category1,name="document_sous_category1"),
     ################################################################################################
    # path('ajouter-soucategorie1/<int:id>',test1.as_view(),name="ajouter-souscategorie1"),
    #####################################################################################################
    # path('ajouter-un-document/<str:chaine>',test2,name="ajouter"),
    ############        AJOUT D UNE SOUCATEGORIE ###################
    path('ajouter-soucategorie1/<str:id>',test2,name="ajouter-souscategorie1"),
    ############        AJOUT D UNE SOUCATEGORIE (la seoeur) ###################
    path('ajouter-docu/<str:id>',ajout_document,name="ajouter-docu"),
    path('modifier-docu/<str:id>',modifier_document,name="modifier-docu"),
    # path('ajouter-doc',test3,name="ajouter-doc"),
]
