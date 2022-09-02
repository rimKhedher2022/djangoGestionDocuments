from django.contrib import admin

# Register your models here.
from .models import Institution, Matiere, Subcategorie, Document

admin.site.register(Document)
admin.site.register(Subcategorie)
admin.site.register(Institution)
admin.site.register(Matiere)