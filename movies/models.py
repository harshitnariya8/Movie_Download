from django.db import models
from datetime import datetime


# Create your models here.
class NewMovie(models.Model):
    Movie_Name = models.CharField(max_length=300, blank=False)
    Description = models.TextField()
    Trailer = models.CharField(max_length=250, blank=False)
    Download_link = models.CharField(max_length=233, blank=False)
    Director = models.CharField(max_length=233, blank=False)
    Writer = models.CharField(max_length=233, blank=False)
    Star_Cast = models.CharField(max_length=400, blank=False)
    genres = models.CharField(max_length=300, blank=False)
    Realese_Date = models.DateField(blank=False)
    Run_time = models.IntegerField(blank=False)
    Plot_keywords = models.CharField(max_length=233, blank=False)
    Poster = models.ImageField(upload_to='media/movies/%y/%m/')
    Sample1 =models.ImageField(upload_to='media/sample1/%y/%m/')
    Sample2 = models.ImageField(upload_to='media/sample2/%y/%m/')
    Sample3 = models.ImageField(upload_to='media/sample3/%y/%m/')
    Rating = models.FloatField(max_length=10)
    webSearies=models.BooleanField(default=False)
    Featured = models.BooleanField(default=False)
    Coming_Soon = models.BooleanField(default=False)
    Created_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.Movie_Name
