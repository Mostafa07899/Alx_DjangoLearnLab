# Generated by Django 5.1.2 on 2024-11-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('librarian', 'Librarian'), ('member', 'Member')], max_length=20),
        ),
    ]
