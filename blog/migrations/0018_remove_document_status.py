# Generated by Django 4.1 on 2022-09-02 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_document_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='status',
        ),
    ]
