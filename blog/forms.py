from email.policy import default
from optparse import Option
from urllib import request
from urllib.request import urlopen
from django import forms 
from .models import Document, Subcategorie,Matiere,Institution,User




class DocumentForm(forms.ModelForm):
    # model_to_filter = CustomModelFilter(queryset=Document.objects.filter(user='rim'))

    class Meta:
        model=Document
        fields=('titre','description','fichier','institution','annee','matiére','Subcategorie')
        labels={'titre':'Titre','description':'description','fichier':'fichier','institution':'institution','annee':'année','matiére':'matiére','Subcategorie':'Subcategorie'}
        widgets={  
                    'titre':forms.TextInput(attrs={'class':'form-control'}),
                    'description':forms.Textarea(attrs={'class':'form-control'}),
                    'fichier':forms.FileInput(attrs={'class':'form-control'}),
                    'institution':forms.Select(attrs={'class':'form-control'}),
                    'annee':forms.TextInput(attrs={'class':'form-control'}),
                    'matiére':forms.Select(attrs={'class':'form-control'}),
                    'Subcategorie':forms.Select(attrs={'class':'form-control','rows':5}),
        } 

    def __init__(self, user, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['Subcategorie'].queryset = Subcategorie.objects.filter(user=user)
        self.fields['institution'].queryset = Institution.objects.filter(user=user)
        self.fields['matiére'].queryset = Matiere.objects.filter(user=user)   
      




class SubcategorieForm(forms.ModelForm):
    class Meta:
        model=Subcategorie
        fields=('titre_categorie','desc')
        # if (="")
        labels={'titre_categorie':'Titre','desc':'description','parent':'parent'}
        widgets={
            'titre_categorie':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control','rows':5}),
            'parent':forms.TextInput(attrs={'class':'form-control','rows':5}),
        }



class SubcategorieForm1(forms.ModelForm):
  
    # def __init__(self, *args, **kwargs):
    #     super(SubcategorieForm1, self).__init__(*args, **kwargs)
    #     self.fields['parent'].initial = '4'

    class Meta:
        model=Subcategorie
        fields=('titre_categorie','desc','parent','user')
        labels={'titre_categorie':'Titre','desc':'description','parent':'parent'}
        widgets={
            'titre_categorie':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control','rows':5}),
            'parent':forms.TextInput(attrs={'class':'form-control'}),
        }

class MatiereForm(forms.ModelForm):
  
    # def __init__(self, *args, **kwargs):
    #     super(SubcategorieForm1, self).__init__(*args, **kwargs)
    #     self.fields['parent'].initial = '4'

    class Meta:
        model=Matiere
        fields=('matiére','filiére','coefficient')
        labels={'matiére':'matiére','filiére':'filiére','coefficient':'coefficient'}
        widgets={
            'matiére':forms.TextInput(attrs={'class':'form-control'}),
            'filiére':forms.TextInput(attrs={'class':'form-control'}),
            'coefficient':forms.TextInput(attrs={'class':'form-control'}),
           
        }
class InstitutionForm(forms.ModelForm):
  
    # def __init__(self, *args, **kwargs):
    #     super(SubcategorieForm1, self).__init__(*args, **kwargs)
    #     self.fields['parent'].initial = '4'

    class Meta:
        model=Institution
        fields=('Institut','ville',)
        labels={'Institut':'Institut', 'ville':'ville'}
        widgets={
            'Institut':forms.TextInput(attrs={'class':'form-control'}),
            'ville':forms.TextInput(attrs={'class':'form-control'}),
           
        }





    

        