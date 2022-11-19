from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'merry_day'

urlpatterns = [
    path("",login, name = "login"),
    path("main/", main, name = "main"),
    path("card_detail/<int:date>/", card_detail, name = "detail"),
    path("share/",share,name = "share"),
]
