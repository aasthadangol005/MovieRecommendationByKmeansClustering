# Generated by Django 3.2.3 on 2021-06-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0006_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='original_title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.TextField(),
        ),
    ]
