from urllib import request

from .models import *
import django_filters


     

class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model= Document

        fields=('titre','description','institution','annee','matiére','Subcategorie')


