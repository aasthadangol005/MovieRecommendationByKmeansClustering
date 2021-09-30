from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieList
        fields = ('id','genre','title','original_title')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('movieId','userId','rating')


class PopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularMovies
        fields = ('id','genre','title','original_title')