# Generated by Django 3.2.3 on 2021-06-06 09:12

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movieapp', '0018_auto_20210606_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', multiselectfield.db.fields.MultiSelectField(choices=[{'Animation': 'Animation', 'id': 16}, {'Comdey': 'Comedy', 'id': 35}, {'Family': 'Family', 'id': 10751}, {'Romance': 'Romance', 'id': 10749}, {'Crime': 'Crime', 'id': 80}, {'Drama': 'Drama', 'id': 18}, {'Action': 'Action', 'id': 28}, {'Thriller': 'Thriller', 'id': 53}, {'Mystery': 'Mystery', 'id': 9648}, {'War': 'War', 'id': 10752}, {'Adventure': 'Adventure', 'id': 12}, {'History': 'History', 'id': 36}, {'Foreign': 'Foreign', 'id': 10769}, {'Horror': 'Horror', 'id': 27}, {'Documentary': 'Documentary', 'id': 99}, {'Music': 'Music', 'id': 10402}, {'Science Fiction': 'Science Fiction', 'id': 878}, {'TV Movie': 'TV Movie', 'id': 10770}, {'Western': 'Western', 'id': 37}, {'Fantasy': 'Fantasy', 'id': 14}], max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('popularity', models.FloatField(blank=True)),
                ('title', models.TextField(blank=True)),
                ('vote_average', models.FloatField(blank=True)),
                ('vote_count', models.FloatField(blank=True)),
                ('genres', models.ManyToManyField(to='movieapp.MovieGenre')),
            ],
        ),
    ]
