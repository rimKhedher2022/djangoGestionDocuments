from django.contrib import admin

# Register your models here.
from .models import Categorie, Document

admin.site.register(Document)
admin.site.register(Categorie)