from django.shortcuts import render
from django.contrib.auth.models import User

from datetime import datetime
from data.views import create_contents, get_user_content

def login(request):
    return render(request, "login.html")
    
def main(request):

    return render(request, "main.html")

def card_detail(request, date):
    user = request.user
    today = datetime.today().day
    if today == date:
        create_contents(user.id)
    context = get_user_content(user.id, date)
    return render(request, "song.html", context)

def share(request, date):
    user = request.user
    context = get_user_content(user.id, date)
    return render(request, "share_04.html", context)