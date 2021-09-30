# Generated by Django 3.2.3 on 2021-06-06 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0011_auto_20210605_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='overview',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tagline',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movieapp.MovieGenre'),
        ),
    ]