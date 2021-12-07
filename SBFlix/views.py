from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import serializers, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.core.exceptions import ValidationError


# Create your views here.
class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializers = MovieSerializer(queryset, many=True)
        return Response({
            "status" : 200,
            "message" : "Success",
            "data":serializers.data
        })
    
    def perform_create(self, serializer):
        try:
            queryset = Movie.objects.filter(title=self.request.data["title"])
            if queryset.exists():
                # handle if the movie is already exists
                raise ValidationError('the movie is already exists')
        except AttributeError:
            pass
        serializer.save()

class MovieFilter(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title','genre','likes']
    ordering_fields = ['title','genre','likes']
    # url/SBFlix/filter/?ordering=genre,-likes,title to get query grouped by genre, ordered by likes desc and title asc
    
class MovieSearch(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    # url/SBFlix/search/?search=movietitle change the movietitle according to the title you want to search
    
class MovieDestroyView(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class Likes(APIView):
    def put(self, request, id):
        try :
            movie = Movie.objects.get(id=id)
            movie.likes += 1
            movie.save()
        except Movie.DoesNotExist:
             return Response({
                "error" : "movie doesn't exist"
            })

        serializers = MovieSerializer(movie)
        return Response({
            "status" : 201,
            "message" : "liked",
            "data" : serializers.data
        }, status=status.HTTP_201_CREATED)


class Dislikes(APIView):
    def put(self, request, id):
        try :
            movie = Movie.objects.get(id=id)
            movie.likes += 1
            movie.save()
        except Movie.DoesNotExist:
             return Response({
                "error" : "movie doesn't exist"
            })

        serializers = MovieSerializer(movie)
        return Response({
            "status" : 201,
            "message" : "disliked",
            "data" : serializers.data
        }, status=status.HTTP_201_CREATED)
