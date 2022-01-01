from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('movielist/',views.movielist,name='movielist'),
    path('<int:id>',views.movie_details,name='movie_details'),
]