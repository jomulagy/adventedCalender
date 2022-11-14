from django.db import models

class MovieTitles(models.Model):
    title = models.CharField(max_length=100,null=False,default = "")

class Movie(models.Model):
    title = models.CharField(max_length=100, null = False, default = '')
    image = models.ImageField(upload_to= 'movies')
    memo = models.CharField(null = False, max_length = 200)
    link = models.CharField(null = False, max_length = 100)

class Music(models.Model):
    title = models.CharField(max_length=100, null = False, default = '')
    image = models.ImageField(upload_to= 'movies')
    memo = models.CharField(null = False, max_length = 200)
    link = models.CharField(null = False, max_length = 100)
    
