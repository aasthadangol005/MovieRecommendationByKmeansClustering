# Generated by Django 3.2.3 on 2021-10-01 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0077_ratingmovies_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user',
        ),
        migrations.DeleteModel(
            name='RatingMovies',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
