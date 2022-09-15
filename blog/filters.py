from random import choices
from telnetlib import SE
from typing_extensions import Self
from urllib import request



from blog.models import Subcategorie , Matiere ,Institution
from blog.forms import DocumentForm
from .models import *
import django_filters
from django import forms 
import urllib3

class DocumentFilter(django_filters.FilterSet):
   
    titre = django_filters.CharFilter(
        lookup_expr='icontains',
         widget=forms.TextInput(attrs={'class': 'form-control'}),
        )
    
  

    annee = django_filters.ModelChoiceFilter(
        field_name='annee',
        queryset=Année.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )



 

    description = django_filters.CharFilter(
        lookup_expr='icontains',
         widget=forms.TextInput(attrs={'class': 'form-control'}),
  
    )


    matiére = django_filters.ModelChoiceFilter(
        field_name='matiére', 
      
        queryset=Matiere.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    Subcategorie = django_filters.ModelChoiceFilter(
        field_name='Subcategorie', 
        queryset = Subcategorie.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )


    institution = django_filters.ModelChoiceFilter(
        field_name='institution', 
        queryset= Institution.objects.all(),
       
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

  


   
   



   
    class Meta:
        model = Document
        fields=['titre','description','institution','annee','matiére','Subcategorie']

  


        # widgets={  
        #             'titre':forms.TextInput(attrs={'class':'form-control'}),
        #             'description':forms.Textarea(attrs={'class':'form-control'}),
        #             # 'fichier':forms.FileInput(attrs={'class':'form-control'}),
        #             'institution':forms.Select(attrs={'class':'form-control'}),
        #             'annee':forms.TextInput(attrs={'class':'form-control'}),
        #             'matiére':forms.Select(attrs={'class':'form-control'}),
        #             'Subcategorie':forms.Select(attrs={'class':'form-control','rows':5}),
        # } 
    

