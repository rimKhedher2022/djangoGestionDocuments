from django.contrib import admin

# Register your models here.
from .models import Subcategorie, Document

admin.site.register(Document)
admin.site.register(Subcategorie)