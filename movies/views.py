import datetime

from .models import NewMovie
from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
    movies = NewMovie.objects.order_by('-Realese_Date').filter(Coming_Soon=False)
    featured_movies = NewMovie.objects.order_by('-Created_date').filter(Featured=True)
    top_rated = NewMovie.objects.order_by('Rating').reverse()
    Bollywood_movies = NewMovie.objects.filter(Plot_keywords__icontains='Bollywood')
    Coming_Soon_Movies = NewMovie.objects.filter(Coming_Soon=True).order_by('-Created_date').reverse()
    Movie_search = NewMovie.objects.values_list('Movie_Name',flat=False).distinct()
    if 'Movie_Name' is request.GET:
        Movie_Name = request.GET['Movie_Name']
        if Movie_Name:
            movies = movies.filter(Movie_Name__contains=Movie_Name)
    data = {
        'movies': movies,
        'featured_movies' : featured_movies,
        'top_rated' : top_rated,
        'Bollywood_movies' : Bollywood_movies,
        'Coming_Soon_Movies' : Coming_Soon_Movies,
    }
    return render(request, 'home.html', data,)


def movie_details(request,id):
    movies = NewMovie.objects.order_by('-Created_date')
    movie_single = get_object_or_404(NewMovie, pk=id)
    mov = movie_single.genres.split()

    for m in mov:
        related_movie = NewMovie.objects.filter(genres__icontains=m)

    movies_count = related_movie.count()
    data = {
            'movies' : movies,
            'movie_single': movie_single,
            'related_movie' : related_movie,
            'movies_count' : movies_count,

    }
    return render(request, 'movies/movie_details.html',data)


def movielist(request):
    movies = NewMovie.objects.order_by('-Realese_Date')
    movies_count = movies.count()
    movie_search = NewMovie.objects.values_list('Movie_Name',flat=True).distinct()

    if 'Movie_Name' in request.GET:
        Movie_Name = request.GET['Movie_Name']
        if Movie_Name:
            movies = movies.filter(Movie_Name__icontains=Movie_Name)
            movies_count = movies.count()
    data = {
        'movies': movies,
        'movies_count' : movies_count,
        'movie_search' : movie_search,
    }
    return render(request, 'movielist.html', data)


