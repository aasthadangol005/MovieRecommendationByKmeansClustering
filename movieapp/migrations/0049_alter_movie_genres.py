# Generated by Django 3.2.3 on 2021-06-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0048_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, to='movieapp.MovieGenre'),
        ),
    ]