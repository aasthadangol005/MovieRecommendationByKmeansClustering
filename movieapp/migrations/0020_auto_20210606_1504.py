# Generated by Django 3.2.3 on 2021-06-06 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0019_moviegenre_movielist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielist',
            name='genres',
        ),
        migrations.DeleteModel(
            name='MovieGenre',
        ),
        migrations.DeleteModel(
            name='MovieList',
        ),
    ]