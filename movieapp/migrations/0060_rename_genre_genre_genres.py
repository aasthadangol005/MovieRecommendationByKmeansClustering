# Generated by Django 3.2.3 on 2021-06-13 17:03

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('movieapp', '0059_rename_genres_genre_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='genres',
        ),
    ]
