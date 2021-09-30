# Generated by Django 3.2.3 on 2021-06-09 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0030_delete_popularmovies'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PopularMovies',
            fields=[
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('popularity', models.FloatField()),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
                ('genres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.moviegenre')),
            ],
        ),
    ]
