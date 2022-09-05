from urllib import request

from blog.forms import DocumentForm

from .models import *
import django_filters
from django import forms 

class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = Document
        fields=('titre','description','institution','annee','matiére','Subcategorie')
        labels={'titre':'Titre','description':'description','institution':'institution','annee':'année','matiére':'matiére','Subcategorie':'Subcategorie'}
        def __init__(self, user, *args, **kwargs):

            super(Document, self).__init__(*args, **kwargs)
            self.fields['Subcategorie'].queryset = Subcategorie.objects.filter(user=user)
            self.fields['institution'].queryset = Institution.objects.filter(user=user)
            self.fields['matiére'].queryset = Matiere.objects.filter(user=user) 
            
        widgets={  
                    'titre':forms.TextInput(attrs={'class':'form-control'}),
                    'description':forms.Textarea(attrs={'class':'form-control'}),
                    # 'fichier':forms.FileInput(attrs={'class':'form-control'}),
                    'institution':forms.Select(attrs={'class':'form-control'}),
                    'annee':forms.TextInput(attrs={'class':'form-control'}),
                    'matiére':forms.Select(attrs={'class':'form-control'}),
                    'Subcategorie':forms.Select(attrs={'class':'form-control','rows':5}),
        } 
    

