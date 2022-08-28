from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=('titre','description','fichier','institution','annee','matiére','categorie')
        labels={'titre':'Titre','description':'description','fichier':'fichier','institution':'institution','annee':'année','matiére':'matiére','categorie':'categorie'}
        widgets={
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'fichier':forms.FileInput(attrs={'class':'form-control'}),
            'institution':forms.TextInput(attrs={'class':'form-control'}),
            'annee':forms.TextInput(attrs={'class':'form-control'}),
            'matiére':forms.TextInput(attrs={'class':'form-control'}),
            'categorie':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':5}),
        }


        