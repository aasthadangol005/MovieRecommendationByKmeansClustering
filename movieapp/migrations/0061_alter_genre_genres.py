# Generated by Django 3.2.3 on 2021-06-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0060_rename_genre_genre_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genres',
            field=models.CharField(max_length=200, primary_key='True', serialize=False),
        ),
    ]
