# Generated by Django 3.2.3 on 2021-06-11 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0047_rename_name_moviegenre_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
                ('genres', models.ManyToManyField(blank=True, to='movieapp.PopularMovies')),
            ],
        ),
    ]
