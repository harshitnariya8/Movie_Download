from django.contrib import admin
from .models import NewMovie


# Register your models here.

class MvAdmin(admin.ModelAdmin):
    list_display = ('id', 'Movie_Name', 'Featured','genres')
    list_editable = ('Featured',)


admin.site.register(NewMovie, MvAdmin)
