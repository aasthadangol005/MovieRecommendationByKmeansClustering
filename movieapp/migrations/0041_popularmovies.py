# Generated by Django 3.2.3 on 2021-06-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0040_delete_popularmovie'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularMovies',
            fields=[
                ('genres', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
            ],
        ),
    ]
