# Generated by Django 3.2.3 on 2021-06-09 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0032_auto_20210609_1023'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PopularMovies',
        ),
    ]