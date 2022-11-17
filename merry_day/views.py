from django.shortcuts import render
from django.contrib.auth.models import User

from datetime import datetime
from data.views import create_contents, get_user_content
def main(request):

    return render(request, "test.html")

def card_detail(request, date):
    #user = request.user
    user = User.objects.get(id = 1)
    today = datetime.today().day
    if today == date:
        create_contents(user.id)
    context = get_user_content(user.id,date)
    print(context)
    return render(request, "test.html", context)