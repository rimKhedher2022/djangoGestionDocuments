# Generated by Django 4.1 on 2022-09-07 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_année'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='annee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.année'),
        ),
    ]
