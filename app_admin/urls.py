import imp
from django.urls import path
from .views import *

urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('mes-documents',user_documents,name="mes-documents"),
    path('ajouter-document',addDocument.as_view(),name="ajouter-document"),
]
