# Generated by Django 3.2.3 on 2021-06-09 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0031_moviegenre_popularmovies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popularmovies',
            name='genres',
        ),
        migrations.DeleteModel(
            name='MovieGenre',
        ),
    ]
