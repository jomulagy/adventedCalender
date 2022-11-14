from django.shortcuts import render

from .models import MovieTitles, Movie

import random
import os
import sys
import requests
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_titles(request):
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
    return render(request, "test.html")

def get_content(request):
    
    client_id = "WBizd3AjzRS6rm8IoYHJ"
    client_secret = "ptArHpcM6x"

    num = random.randint(0,300)
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

    title = data['items'][0]['title'].strip("</b>")
    print(title)
    link = data['items'][0]['link']
    date = data['items'][0]['pubDate']
    director = data['items'][0]['director'].split("|")[0]
    print(director)
    
    actors = data['items'][0]['actor'].split("|")[:-1]
    rating = float(data['items'][0]['userRating'])

    return render(request, "test.html")
