# Generated by Django 3.2.3 on 2021-06-05 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0007_auto_20210605_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='vote_average',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='vote_count',
            field=models.FloatField(),
        ),
    ]
