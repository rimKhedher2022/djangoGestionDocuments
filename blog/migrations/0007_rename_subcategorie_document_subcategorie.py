# Generated by Django 4.1 on 2022-08-29 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_categorie_subcategorie_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='subCategorie',
            new_name='Subcategorie',
        ),
    ]
