from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import serializers, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.core.exceptions import ValidationError


# Create your views here.
class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['title','genre']
    ordering_fields = ['title','genre']
    search_fields = ['title']
    
class MovieCreateView(CreateAPIView):
    serializer_class = MovieSerializer
    Response(status=status.HTTP_201_CREATED)
    
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