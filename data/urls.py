from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'data'

urlpatterns = [
    path('get_titles/', get_titles, name = "get_titles"),
    path('get_content/',get_content, name = "get_content"),
]
