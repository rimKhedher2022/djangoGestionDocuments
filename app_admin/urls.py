import imp
from django.urls import path
from .views import *

urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('mes-documents',user_documents,name="mes-documents"),
    path('ajouter-document',addDocument.as_view(),name="ajouter-document"),
    path('modifier-document/<int:pk>',UpdateDocument.as_view(),name="modifier-document"),
    path('supprimer-document/<int:pk>',DeleteDocument.as_view(),name="supprimer-document"),
    path('document_sous_category/<str:soucat>',Document_sous_category,name="document_sous_category"),
    path('modifier-souscategorie/<int:pk>',UpdateSouscategorie.as_view(),name="modifier-souscategorie"),
    path('supprimer-souscategorie/<int:pk>',DeleteSouscategorie.as_view(),name="supprimer-souscategorie"),
     path('ajouter-souscategorie',addSouscategorie.as_view(),name="ajouter-souscategorie"),
]
