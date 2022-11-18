from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("data/", include('data.urls')),
    path("", include('merry_day.urls')),
    re_path(r'^account/', include('allauth.urls')),
]
