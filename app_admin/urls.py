import imp
from django.urls import path
from .views import *

urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('mes-documents',user_documents,name="mes-documents"),
    path('ajouter-document',addDocument.as_view(),name="ajouter-document"),
    path('modifier-document/<int:pk>',UpdateDocument.as_view(),name="modifier-document"),
    path('supprimer-document/<int:pk>',DeleteDocument.as_view(),name="supprimer-document"),
]
