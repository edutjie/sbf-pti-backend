from rest_framework import serializers
from SBFlix.models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'poster', 'trailer', 'genre', 'release_year','likes', 'dislikes']