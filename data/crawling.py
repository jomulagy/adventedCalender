from data.models import Music_data
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=452125047#params%5BplylstSeq%5D=452125047&po=pageObj&startIndex=1")
browser.maximize_window()
for i in range (0,51):
    new = Music_data.objects.create()
    new.title = browser.find_element(By.XPATH,'//*[@id="frm"]/div/table/tbody/tr['+str(i)+']/td[5]/div/div/div[1]/span/a').text
    try:
        artist = browser.find_element(By.XPATH,'//*[@id="frm"]/div/table/tbody/tr['+str(i)+']/td[5]/div/div/div[2]/a').text
        new.artist = artist
    except:
        new.artist = "Various Artist"
    new.image = browser.find_element(By.XPATH,'//*[@id="frm"]/div/table/tbody/tr['+str(i)+']/td[3]/div/a/img').get_attribute("src")
    
    browser.find_element(By.XPATH,'//*[@id="frm"]/div/table/tbody/tr['+str(i)+']/td[3]/div/a').click()
    time.sleep(1)
    new.link = browser.current_url
    new.save()
    browser.back()
    time.sleep(1)
browser.close()