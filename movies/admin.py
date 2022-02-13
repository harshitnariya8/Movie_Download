from django.contrib import admin
from .models import NewMovie


# Register your models here.

class MvAdmin(admin.ModelAdmin):
    list_display = ('id', 'Movie_Name', 'Featured','webSearies','Plot_keywords')
    list_editable = ('Featured','webSearies','Plot_keywords')


admin.site.register(NewMovie, MvAdmin)
