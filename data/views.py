from django.shortcuts import render
from django.contrib.auth.models import User

from .models import MovieTitles, Movie, Music_data, Music_content

import random
import requests
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#메인
def home(request):
    return render(request, "test.html")
#조회하기
def get_user_content(user_id, date):
    user = User.objects.get(id = user_id)
    if user.Movie.filter(date__day = str(date)).exists():
        content = user.Movie.filter(date__day = str(date))[0]
        context = {
            "type" : "movie",
            "image" : content.image,
            "title" : content.title,
            "director" : content.director,
            "rating" : content.rating,
            "link" : content.link,
        }
        
    elif user.Music.filter(date__day = str(date)).exists():
        content = user.Music.filter(date__day = str(date))[0]
        context = {
            "type" : "music",
            "image" : content.image,
            "title" : content.title,
            "director" : content.director,
            "link" : content.link,
        }
    
    return context

#새로 만들기
def create_contents(user_id):
    today = datetime.today()
    user = User.objects.get(id = user_id)
    if Movie.objects.filter(user = user, date__day = today.day).exists() or Music_content.objects.filter(user = user, date__day = today.day).exists():
        return

    num = random.randint(0,1)
    if num == 0 :
        new = Movie()
        data = get_movie()
        new.user = user 
        new.title = data['title']
        new.image = data['image']
        new.director = data['director']
        new.link = data["link"]
        new.actors = data['actors']
        new.year = data['date']
        new.rating = data['rating']
        new.save()
    else:
        new = Music_content()
        data = get_music()
        new.user = user
        new.title = data['title']
        new.image = data['image']
        new.director = data['artist']
        new.link = data["link"]
        new.save()
    return

def get_titles():
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get("https://www.netflix.com/browse")
    browser.maximize_window()


    id = browser.find_element(By.XPATH,'//*[@id="id_userLoginId"]')
    id.send_keys("jomulagy988@gmail.com")
    pwd = browser.find_element(By.XPATH,'//*[@id="id_password"]')
    pwd.send_keys("kjhkjs1004@")
    browser.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
    time.sleep(3)

    browser.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a').click()
    time.sleep(1)

    browser.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/button').click()
    search = browser.find_element(By.XPATH,'//*[@id="searchInput"]')
    search.send_keys("크리스마스")
    search.send_keys(Keys.ENTER)
    time.sleep(3)

    SCROLL_PAUSE_SEC = 2

    # 스크롤 높이 가져옴
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # 끝까지 스크롤 다운
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 1초 대기
        time.sleep(SCROLL_PAUSE_SEC)

        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    for i in range(0,300):
        title = browser.find_element(By.XPATH,'//*[@id="title-card-0-'+str(i)+'"]/div[1]/a/div[1]/div/p').text
        new = MovieTitles(title = title)
        new.save()

    browser.close()


def get_movie():
    actr = ''
    while True:
        client_id = "WBizd3AjzRS6rm8IoYHJ"
        client_secret = "ptArHpcM6x"

        num = random.randint(1,300)
        title = MovieTitles.objects.get(id = num).title

        movie = title
        header_parms = {
            "X-Naver-Client-Id" : client_id,
            "X-Naver-Client-Secret" : client_secret
        }
        url = f"https://openapi.naver.com/v1/search/movie.json?query={movie}"
        res = requests.get(url,headers=header_parms)
        data = res.json()
        # 있는지 검사하기
        
        if data['items']:
            break
    
    title = data['items'][0]['title'].strip("</b>")
    title = title.replace("<b>","")
    title = title.replace("</b>","")

    image = data['items'][0]['image']
    link = data['items'][0]['link']
    date = data['items'][0]['pubDate']
    director = data['items'][0]['director'].split("|")[0]
    director = director.replace("<b>","")
    director = director.replace("</b>","")

    actors = data['items'][0]['actor'].split("|")[:-1]
    for actor in actors:
        actr = actr + actor + " "
    rating = float(data['items'][0]['userRating'])

    context = {
        "title" : title,
        "image" : image,
        "link" : link,
        "date" : date,
        "director" : director,
        "actors" : actr,
        "rating" : rating,
    }
    return context

def music_data(request):
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get("https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=452125047#params%5BplylstSeq%5D=452125047&po=pageObj&startIndex=1")
    browser.maximize_window()

    for i in range (1,51):
        new = Music_data.objects.create()
        new.title = browser.find_element(By.XPATH,'//*[@id="frm"]/div/table/tbody/tr['+str(i)+']/td[5]/div/div/div[1]/span/a').text
        try:
            artist = browser.find_element(By.XPATH,'//*[@id="frm"]/div/table/tbody/tr['+str(i)+']/td[5]/div/div/div[2]/a').text
            new.artist = artist
        except:
            new.artist = "Various Artist"
        browser.find_element(By.XPATH,'//*[@id="frm"]/div/table/tbody/tr['+str(i)+']/td[3]/div/a').click()
        new.image = browser.find_element(By.XPATH,'//*[@id="d_album_org"]/img').get_attribute("src")
        
        time.sleep(1)
        new.link = browser.current_url
        new.save()
        browser.back()
        time.sleep(1)

    browser.close()

def get_music():
    num = random.randint(58,108)
    new = Music_data.objects.get(id = num)

    context = {
        "id" : new.id,
        "title" : new.title,
        "artist" : new.artist,
        "image" : new.image,
        "link" : new.link,
    }
    return context   
