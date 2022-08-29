from django import forms
from .models import Document, Subcategorie

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=('titre','description','fichier','institution','annee','matiére','Subcategorie')
        labels={'titre':'Titre','description':'description','fichier':'fichier','institution':'institution','annee':'année','matiére':'matiére','Subcategorie':'Subcategorie'}
        widgets={
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'fichier':forms.FileInput(attrs={'class':'form-control'}),
            'institution':forms.TextInput(attrs={'class':'form-control'}),
            'annee':forms.TextInput(attrs={'class':'form-control'}),
            'matiére':forms.TextInput(attrs={'class':'form-control'}),
            'Subcategorie':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':5}),
        }

class SubcategorieForm(forms.ModelForm):
    class Meta:
        model=Subcategorie
        fields=('titre_categorie','desc')
        labels={'titre_categorie':'Titre','desc':'description'}
        widgets={
            'titre_categorie':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control','rows':5}),
        }


        