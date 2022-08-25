from distutils.command import upload
from django.db import models

# Create your models here.
class Categorie(models.Model):
   titre_categorie=models.CharField(max_length=50)
   desc=models.TextField()

   def __str__ (self):
        return self.titre_categorie 

class Document(models.Model):
    titre=models.CharField(max_length=50)
    description=models.TextField()
    fichier=models.FileField()
    institution=models.CharField(max_length=100)
    annee=models.CharField(max_length=4)
    matiére=models.CharField(max_length=50)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE) 
    # une categorie a plusieurs documents

    def __str__ (self):
        return self.titre

       
           