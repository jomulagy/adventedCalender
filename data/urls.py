from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'data'

urlpatterns = [
    path("main", home, name = "home"),
    path("new",create_contents,name = "create_contents"),
    path("crawling/",music_data,name = "music_data")
]
