# Generated by Django 3.2.3 on 2021-06-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0009_auto_20210605_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='original_title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tagline',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.TextField(),
        ),
    ]
