# Generated by Django 4.1 on 2022-09-04 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_document_institution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='institution',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]