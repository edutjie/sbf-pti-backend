from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import status

# Create your views here.
class MovieList(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializers = MovieSerializer(movie, many=True)
        return Response(serializers.data)

    def post(self, request):
        book = Movie.objects.create(
            title = request.data['title'],
            poster = request.data['poster'],
            trailer = request.data['trailer'],
            genre = request.data['genre'],
            release_year = request.data['release_year'],
        )

        serializers = MovieSerializer(book)
        return Response(serializers.data, status=status.HTTP_201_CREATED)