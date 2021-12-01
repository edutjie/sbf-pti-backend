from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieListView.as_view()),
    path('add_movie/', views.MovieCreateView.as_view()),
    path('add_like/<int:id>', views.Likes.as_view()),
    path('add_dislike/<int:id>', views.Dislikes.as_view()),
]