# Generated by Django 3.2.3 on 2021-06-11 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0049_alter_movie_genres'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
