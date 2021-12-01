from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import serializers, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


# Create your views here.
class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title','genre']
    ordering_fields = ['title','genre']
    
class MovieCreateView(CreateAPIView):
    serializer_class = MovieSerializer
    
class MovieDestroyView(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
