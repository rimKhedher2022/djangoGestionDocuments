from unicodedata import category
from blog.models import Categorie, Document
def run():
    for i in range(5,15):
        document=Document()
        categorie=Categorie(1)
        document.titre="Document n #%d" %i
        document.description="Description document n #%d" %i
        document.fichier="pass.pdf"
        document.categorie=categorie
     
        document.delete()
print("opération réussie")        


