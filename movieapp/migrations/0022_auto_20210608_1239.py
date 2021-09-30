# Generated by Django 3.2.3 on 2021-06-08 06:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movieapp', '0021_movielist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielist',
            name='popularity',
        ),
        migrations.RemoveField(
            model_name='movielist',
            name='vote_average',
        ),
        migrations.RemoveField(
            model_name='movielist',
            name='vote_count',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(5)])),
                ('movieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.movielist')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('userId', 'movieId')},
                'index_together': {('userId', 'movieId')},
            },
        ),
    ]