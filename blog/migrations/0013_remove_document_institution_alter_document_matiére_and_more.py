# Generated by Django 4.1 on 2022-09-01 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_matiere_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='institution',
        ),
        migrations.AlterField(
            model_name='document',
            name='matiére',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.matiere'),
        ),
        migrations.AddField(
            model_name='document',
            name='institution',
            field=models.ManyToManyField(to='blog.institution'),
        ),
    ]
