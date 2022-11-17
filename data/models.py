from django.db import models
from django.contrib.auth.models import User

class MovieTitles(models.Model):
    title = models.CharField(max_length=100,null=False,default = "")

class Movie(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE,related_name = "Movie")
    date = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=100, null = False, default = '')
    image = models.ImageField(upload_to= 'movies')
    director = models.CharField(null = False, max_length = 200)
    link = models.CharField(null = False, max_length = 100)
    actors = models.CharField(null = False, max_length = 200)
    year = models.CharField(null = False, max_length = 200)
    rating = models.CharField(null = False, max_length = 200)

class Music_data(models.Model):
    title = models.CharField(max_length=100, null = False, default = '')
    image = models.ImageField(upload_to= 'movies')
    artist = models.CharField(null = False, max_length = 200)
    link = models.CharField(null = False, max_length = 100)

class Music_content(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE,related_name="Music")
    date = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=100, null = False, default = '')
    image = models.ImageField(upload_to= 'movies')
    director = models.CharField(null = False, max_length = 200)
    link = models.CharField(null = False, max_length = 100)
    
