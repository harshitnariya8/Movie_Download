from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('movielist/',views.movielist,name='movielist'),
    path('<int:id>',views.movie_details,name='movie_details'),
    path('newmovie/',views.newmovie,name='newmovie'),
    path('upcoming/',views.upcoming,name='upcoming'),
    path('Bollywood/',views.Bollywood,name='Bollywood'),
    path('Hollywood/',views.Hollywood,name='Hollywood'),
    path('Search/',views.Search,name='Search'),
]