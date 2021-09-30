# Generated by Django 3.2.3 on 2021-06-06 08:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0015_movielist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='genres',
            field=multiselectfield.db.fields.MultiSelectField(choices=[{'Animation': 'Animation', 'id': 16}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}, {'id': 10749, 'name': 'Romance'}, {'id': 80, 'name': 'Crime'}, {'id': 18, 'name': 'Drama'}, {'id': 28, 'name': 'Action'}, {'id': 53, 'name': 'Thriller'}, {'id': 9648, 'name': 'Mystery'}, {'id': 10752, 'name': 'War'}, {'id': 12, 'name': 'Adventure'}, {'id': 36, 'name': 'History'}, {'id': 10769, 'name': 'Foreign'}, {'id': 27, 'name': 'Horror'}, {'id': 99, 'name': 'Documentary'}, {'id': 10402, 'name': 'Music'}, {'id': 878, 'name': 'Science Fiction'}, {'id': 10770, 'name': 'TV Movie'}, {'id': 37, 'name': 'Western'}, {'id': 14, 'name': 'Fantasy'}], max_length=300),
        ),
    ]
