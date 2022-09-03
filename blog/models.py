from audioop import reverse
from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
#  ??????????

# Create your models here.
class Subcategorie(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
   titre_categorie=models.CharField(max_length=50)
   desc=models.TextField()
   parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name="children",
        null=True,
        blank=True,
    )
    

   def __str__ (self):
    return self.titre_categorie

   
class Institution(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   Institut=models.CharField(max_length=50)
   ville=models.CharField(max_length=50)
  

   def __str__ (self):
    return self.Institut   

   def get_absolute_url(self):
        return reverse("les-instituts")  
          
class Matiere(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   matiére=models.CharField(max_length=50,null=True, blank=True)
   filiére=models.CharField(max_length=50,null=True, blank=True)
   coefficient=models.CharField(max_length=50,null=True, blank=True)
  
  

   def __str__ (self):
    return self.matiére  

   def get_absolute_url(self):
        return reverse("les-matiéres")     



product_status=[
    (1,'kilma'),
    (2,'wa7da')
]
        



class Document(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    titre=models.CharField(max_length=50)
   
    description=models.TextField()
    fichier=models.FileField(null=True)
    institution=models.CharField(max_length=50 ,null=True, blank=True)
    # un document appartient a plusieurs institution , une institution a plusieurs documents
    annee=models.CharField(max_length=4,null=True, blank=True)
    matiére=models.ForeignKey(Matiere,on_delete=models.CASCADE,null=True, blank=True)
    # une matiéres a plusieurs documents , un document appartient a une seule matiére
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    Subcategorie = models.ForeignKey(Subcategorie,on_delete=models.CASCADE,null=True, blank=True) 
    # une categorie a plusieurs documents  *** foreign key == many-to-one relationship

    def __str__ (self):
        return self.titre


    def get_absolute_url(self):
        return reverse("mes-documents")    

       
  

          