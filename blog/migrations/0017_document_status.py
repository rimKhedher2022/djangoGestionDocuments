# Generated by Django 4.1 on 2022-09-02 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_document_matiére'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.IntegerField(choices=[(1, 'kilma'), (2, 'wa7da')], default=0),
            preserve_default=False,
        ),
    ]